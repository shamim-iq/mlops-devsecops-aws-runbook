# Owner-Run Rollouts And Prometheus Commands

Run these commands from the implementation repository after Terraform has created the demo EKS cluster and the current shell is allowed to use the deployment profile. Do not commit generated output, kubeconfig content, tokens, account identifiers, or local-only values.

## Variables

```powershell
$env:AWS_PROFILE = "<deployment-aws-profile>"
$env:AWS_REGION = "us-east-1"
$env:EKS_CLUSTER_NAME = "<private-eks-cluster-name>"
$env:ARGO_ROLLOUTS_NAMESPACE = "argo-rollouts"
$env:PROMETHEUS_NAMESPACE = "monitoring"
$env:APP_NAMESPACE = "prediction-api"
$env:APP_RELEASE = "prediction-api"
$env:APP_CHART_PATH = "k8s/apps/prediction-api/chart"
$env:APP_VALUES = "k8s/apps/prediction-api/chart/values-prod.yaml"
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

## Install Argo Rollouts

```powershell
helm repo add argo https://argoproj.github.io/argo-helm
helm repo update argo

helm upgrade --install argo-rollouts argo/argo-rollouts `
  --namespace $env:ARGO_ROLLOUTS_NAMESPACE `
  --create-namespace `
  --wait

kubectl get pods -n $env:ARGO_ROLLOUTS_NAMESPACE
kubectl get crd rollouts.argoproj.io
kubectl get crd analysistemplates.argoproj.io
kubectl get crd analysisruns.argoproj.io
```

## Install Prometheus

```powershell
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update prometheus-community

helm upgrade --install prometheus prometheus-community/prometheus `
  --namespace $env:PROMETHEUS_NAMESPACE `
  --create-namespace `
  --set alertmanager.enabled=false `
  --set prometheus-pushgateway.enabled=false `
  --set server.persistentVolume.enabled=false `
  --wait

kubectl get pods -n $env:PROMETHEUS_NAMESPACE
kubectl get svc prometheus-server -n $env:PROMETHEUS_NAMESPACE
```

## Verify The Chart Renders

```powershell
helm lint $env:APP_CHART_PATH

helm template $env:APP_RELEASE $env:APP_CHART_PATH `
  -f $env:APP_VALUES
```

Confirm the rendered `AnalysisTemplate` points at:

```text
http://prometheus-server.monitoring.svc.cluster.local
```

Confirm the rendered query is:

```text
sum(prediction_api_requests_total) or vector(0)
```

## Verify Rollout Resources After Argo CD Sync

```powershell
kubectl get ns $env:APP_NAMESPACE
kubectl get rollout -n $env:APP_NAMESPACE
kubectl get analysistemplate -n $env:APP_NAMESPACE
kubectl describe rollout prediction-api -n $env:APP_NAMESPACE
```

## Generate Healthy Traffic

Use this only after the application pod is ready.

```powershell
kubectl port-forward -n $env:APP_NAMESPACE svc/prediction-api 8080:80
```

In a second shell:

```powershell
1..30 | ForEach-Object {
  Invoke-RestMethod `
    -Method Post `
    -Uri "http://127.0.0.1:8080/predict" `
    -ContentType "application/json" `
    -Body '{"feature_a":5.1,"feature_b":3.5,"feature_c":1.4}'
}

Invoke-RestMethod -Uri "http://127.0.0.1:8080/metrics"
```

## Verify Analysis And Promotion

```powershell
kubectl get rollout prediction-api -n $env:APP_NAMESPACE
kubectl get analysisrun -n $env:APP_NAMESPACE
kubectl describe analysisrun -n $env:APP_NAMESPACE
kubectl describe rollout prediction-api -n $env:APP_NAMESPACE
```

The rollout passes when the `prediction-request-volume` analysis run succeeds and the rollout reaches healthy promoted state.

## Evidence To Capture

```powershell
kubectl get pods -n $env:ARGO_ROLLOUTS_NAMESPACE
kubectl get svc prometheus-server -n $env:PROMETHEUS_NAMESPACE
kubectl get rollout prediction-api -n $env:APP_NAMESPACE
kubectl get analysisrun -n $env:APP_NAMESPACE
```

Record only resource names, phases, health, and sync status in the evidence project.
