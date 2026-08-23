# Owner-Run Minimal EFK Logging Commands

Run these commands from the runbook repository after confirming the current Kubernetes context is the demo EKS cluster. Do not commit kubeconfig, private values, generated credentials, or command output that includes account-specific values.

## Variables

```powershell
$env:AWS_PROFILE = "<deployment-aws-profile>"
$env:AWS_REGION = "us-east-1"
$env:EKS_CLUSTER_NAME = "<private-eks-cluster-name>"
$env:LOGGING_NAMESPACE = "logging"
$env:APP_NAMESPACE = "prediction-api"
$env:ELASTICSEARCH_RELEASE = "elasticsearch"
$env:FLUENT_BIT_RELEASE = "fluent-bit-collector"
$env:ELASTICSEARCH_CHART_VERSION = "22.1.6"
$env:FLUENT_BIT_COLLECTOR_CHART_VERSION = "1.1.1"
```

## Confirm Cluster Context

```powershell
aws eks update-kubeconfig `
  --region $env:AWS_REGION `
  --name $env:EKS_CLUSTER_NAME `
  --profile $env:AWS_PROFILE

kubectl config current-context
kubectl get nodes
```

Stop if the context or nodes are not the demo EKS cluster.

## Install Elasticsearch And Kibana

The Bitnami Elasticsearch chart is used because Elastic's standalone Helm chart repository is archived. Kibana is enabled as the bundled subchart so the demo uses one small Elasticsearch release rather than separate stack wiring. The values file disables persistence and uses Bitnami Legacy image repositories because the default Bitnami versioned images are no longer always available in the free public catalog.

```powershell
helm upgrade --install $env:ELASTICSEARCH_RELEASE `
  oci://registry-1.docker.io/bitnamicharts/elasticsearch `
  --version $env:ELASTICSEARCH_CHART_VERSION `
  --namespace $env:LOGGING_NAMESPACE `
  --create-namespace `
  --values projects/2026-08-22_minimal-efk-logging/values-elasticsearch-kibana-demo.yaml `
  --wait `
  --timeout 10m

kubectl get pods -n $env:LOGGING_NAMESPACE
kubectl get pvc -n $env:LOGGING_NAMESPACE
kubectl get svc -n $env:LOGGING_NAMESPACE
```

## Apply Short Retention

Keep log data short-lived. Apply this before Fluent Bit starts writing logs so matching indices inherit the one-day delete policy.

```powershell
kubectl run elasticsearch-retention-setup `
  -n $env:LOGGING_NAMESPACE `
  --rm -i --restart=Never `
  --image=curlimages/curl:8.9.1 `
  --command -- sh -c "curl -sS -X PUT http://elasticsearch:9200/_ilm/policy/prediction-api-demo-retention -H 'Content-Type: application/json' -d '{""policy"":{""phases"":{""delete"":{""min_age"":""1d"",""actions"":{""delete"":{}}}}}}}' && curl -sS -X PUT http://elasticsearch:9200/_index_template/prediction-api-logs-template -H 'Content-Type: application/json' -d '{""index_patterns"":[""prediction-api-logs*""],""template"":{""settings"":{""index.lifecycle.name"":""prediction-api-demo-retention""}}}'"
```

## Install Fluent Bit Collector

The collector chart runs Fluent Bit as a DaemonSet and tails Kubernetes container logs. The demo values forward only `prediction-api` namespace logs to Elasticsearch.

```powershell
helm upgrade --install $env:FLUENT_BIT_RELEASE `
  oci://ghcr.io/fluent/helm-charts/fluent-bit-collector `
  --version $env:FLUENT_BIT_COLLECTOR_CHART_VERSION `
  --namespace $env:LOGGING_NAMESPACE `
  --values projects/2026-08-22_minimal-efk-logging/values-fluent-bit-collector-demo.yaml `
  --wait `
  --timeout 5m

kubectl get daemonset -n $env:LOGGING_NAMESPACE
kubectl get pods -n $env:LOGGING_NAMESPACE -l app.kubernetes.io/name=fluent-bit-collector
```

## Verify Logs

```powershell
kubectl get pods -n $env:APP_NAMESPACE
kubectl logs -n $env:LOGGING_NAMESPACE daemonset/$env:FLUENT_BIT_RELEASE --tail=80

kubectl run elasticsearch-log-check `
  -n $env:LOGGING_NAMESPACE `
  --rm -i --restart=Never `
  --image=curlimages/curl:8.9.1 `
  --command -- sh -c "curl -sS 'http://elasticsearch:9200/prediction-api-logs/_search?q=kubernetes.namespace_name:prediction-api&size=3&pretty'"
```

Open Kibana locally only while capturing evidence:

```powershell
kubectl port-forward -n $env:LOGGING_NAMESPACE svc/elasticsearch-kibana 5601:5601
```

In Kibana, create a data view for `prediction-api-logs*` and verify recent application logs from the `prediction-api` namespace.

## Evidence To Capture

```powershell
helm list -n $env:LOGGING_NAMESPACE
kubectl get pods -n $env:LOGGING_NAMESPACE
kubectl get pvc -n $env:LOGGING_NAMESPACE
kubectl get daemonset -n $env:LOGGING_NAMESPACE
kubectl get svc -n $env:LOGGING_NAMESPACE
```

Record only non-sensitive release names, resource names, pod readiness, PVC size, and the Kibana verification result in the evidence project.

## Cleanup

Run cleanup after evidence is captured.

```powershell
helm uninstall $env:FLUENT_BIT_RELEASE -n $env:LOGGING_NAMESPACE
helm uninstall $env:ELASTICSEARCH_RELEASE -n $env:LOGGING_NAMESPACE

kubectl delete pvc -n $env:LOGGING_NAMESPACE -l app.kubernetes.io/instance=$env:ELASTICSEARCH_RELEASE
kubectl delete namespace $env:LOGGING_NAMESPACE
```
