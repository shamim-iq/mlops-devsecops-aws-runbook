# GitOps Repository Structure Checklist

## Repository

| Field | Value |
|---|---|
| Implementation repository URL | `<implementation-repository-url>` |
| Default branch | `main` |
| Repository model | Single repository for app, Terraform, CI, docs, and Kubernetes desired state |
| Argo CD source path | `k8s/apps/prediction-api/overlays/prod` |
| Environment layout | `prod` only for the demo |

## Required Structure

| Area | Path | Status |
|---|---|---|
| Prediction API base manifests | `k8s/apps/prediction-api/base/` | Placeholder pushed |
| Production overlay | `k8s/apps/prediction-api/overlays/prod/` | Placeholder pushed |
| Argo Rollouts resources | `k8s/apps/prediction-api/base/rollout.yaml` | Defined, not pushed |
| Prometheus analysis templates | `k8s/apps/prediction-api/base/analysis-template.yaml` | Defined, not pushed |
| Argo CD install notes | `k8s/platform/argocd/install-notes.md` | Placeholder pushed |
| Argo Rollouts install notes | `k8s/platform/argo-rollouts/install-notes.md` | Placeholder pushed |
| Prometheus install notes | `k8s/platform/prometheus/install-notes.md` | Placeholder pushed |
| EFK install notes | `k8s/platform/efk/install-notes.md` | Placeholder pushed |
| General install notes | `docs/install-notes.md` | Placeholder pushed |

Do not build the CD workflow until the placeholder Kubernetes files are replaced with valid manifests and the Argo CD source path contains a valid Kustomize tree.
