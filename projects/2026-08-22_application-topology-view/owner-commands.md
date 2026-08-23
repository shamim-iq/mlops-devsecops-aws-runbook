# Application Topology View Owner Commands

These commands are for the owner to run in the implementation repository. They do not deploy or delete resources by themselves, except the optional RBAC apply step, which must use approved deployment access.

## Local Implementation Skeleton

Run from `<local-implementation-repo>`.

```powershell
mkdir topology
mkdir topology\topology_view
mkdir topology\reports
New-Item topology\topology_view\__init__.py -ItemType File
New-Item topology\apps.yaml -ItemType File
New-Item topology\topology_view\cli.py -ItemType File
New-Item topology\topology_view\config.py -ItemType File
New-Item topology\topology_view\discover.py -ItemType File
New-Item topology\topology_view\graph.py -ItemType File
New-Item topology\topology_view\render_markdown.py -ItemType File
```

Add this starter config to `topology/apps.yaml`, then adjust only non-sensitive values if the live namespace or selector differs.

```yaml
apps:
  - name: prediction-api
    namespace: prediction-api
    selector:
      app.kubernetes.io/name: prediction-api
```

Add runtime dependencies to the implementation repository dependency file:

```text
kubernetes
PyYAML
```

## Read-Only RBAC Candidate

Create `k8s/platform/topology-viewer/read-only-rbac.yaml` in the implementation repository if the topology tool needs a dedicated identity.

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: topology-viewer
  namespace: prediction-api
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: topology-viewer-read-only
  namespace: prediction-api
rules:
  - apiGroups: [""]
    resources: ["pods", "services", "configmaps", "secrets", "persistentvolumeclaims", "events"]
    verbs: ["get", "list", "watch"]
  - apiGroups: ["apps"]
    resources: ["deployments", "replicasets"]
    verbs: ["get", "list", "watch"]
  - apiGroups: ["networking.k8s.io"]
    resources: ["ingresses"]
    verbs: ["get", "list", "watch"]
  - apiGroups: ["autoscaling"]
    resources: ["horizontalpodautoscalers"]
    verbs: ["get", "list", "watch"]
  - apiGroups: ["argoproj.io"]
    resources: ["rollouts"]
    verbs: ["get", "list", "watch"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: topology-viewer-read-only
  namespace: prediction-api
subjects:
  - kind: ServiceAccount
    name: topology-viewer
    namespace: prediction-api
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: topology-viewer-read-only
```

Owner-only apply command after review:

```powershell
kubectl apply -f k8s\platform\topology-viewer\read-only-rbac.yaml
```

## Verification Commands

Run these only with approved cluster access after the demo cluster exists.

```powershell
kubectl auth can-i list pods --namespace prediction-api
kubectl auth can-i list secrets --namespace prediction-api
kubectl get rollouts.argoproj.io -n prediction-api
kubectl get deploy,rs,pod,svc,ingress,configmap,secret,pvc,hpa,event -n prediction-api
```

Expected result: the owner can list the read-only resources needed for discovery. The output must be reviewed before it is copied into public evidence because Kubernetes object names and event messages can expose environment details.

## Report Generation Target

Use this target command after the CLI exists.

```powershell
python -m topology.topology_view.cli --config topology\apps.yaml --app prediction-api --output topology\reports\prediction-api.md
```

Before adding the report to evidence, scan it:

```powershell
rg -n "[C]:\\|[0-9]{12}|A[K]IA|A[S]IA|arn:aws" topology\reports\prediction-api.md
```

The scan should return no output. Also review the report for secret values, private keys, passwords, tokens, personal identifiers, and local paths before using it as public evidence.
