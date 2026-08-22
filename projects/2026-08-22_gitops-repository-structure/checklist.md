# GitOps Repository Structure Checklist

## Repository

| Field | Value |
|---|---|
| Implementation repository URL | `<implementation-repository-url>` |
| Default branch | `main` |
| Repository model | Single repository for app, Terraform, CI, docs, and Kubernetes desired state |
| Argo CD source path | `k8s/apps/prediction-api/chart` |
| Environment layout | `prod` only for the demo |

## Required Structure

| Area | Path | Status |
|---|---|---|
| Prediction API Helm chart | `k8s/apps/prediction-api/chart/` | Created locally |
| Chart metadata | `k8s/apps/prediction-api/chart/Chart.yaml` | Created locally |
| Default chart values | `k8s/apps/prediction-api/chart/values.yaml` | Created locally |
| Production image values | `k8s/apps/prediction-api/chart/values-prod.yaml` | Created locally |
| Argo Rollouts template | `k8s/apps/prediction-api/chart/templates/rollout.yaml` | Created locally |
| Prometheus analysis template | `k8s/apps/prediction-api/chart/templates/analysis-template.yaml` | Created locally |
| Service template | `k8s/apps/prediction-api/chart/templates/service.yaml` | Created locally |
| Namespace template | `k8s/apps/prediction-api/chart/templates/namespace.yaml` | Created locally |
| Argo CD install notes | `k8s/platform/argocd/install-notes.md` | Filled locally |
| Argo Rollouts install notes | `k8s/platform/argo-rollouts/install-notes.md` | Filled locally |
| Prometheus install notes | `k8s/platform/prometheus/install-notes.md` | Filled locally |
| EFK install notes | `k8s/platform/efk/install-notes.md` | Filled locally |
| General install notes | `docs/install-notes.md` | Filled locally |
| Helm lint | `helm lint .\k8s\apps\prediction-api\chart` | Passed locally |
| Helm render | `helm template prediction-api .\k8s\apps\prediction-api\chart -f .\k8s\apps\prediction-api\chart\values-prod.yaml` | Passed locally |

The Argo CD source path contains a Helm chart that renders locally. Do not build the CD workflow until Terraform defines ECR, EKS, OIDC, and the image tag update path.
