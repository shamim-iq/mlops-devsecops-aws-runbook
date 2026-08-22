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
| Prediction API base manifests | `k8s/apps/prediction-api/base/` | Created locally |
| Production overlay | `k8s/apps/prediction-api/overlays/prod/` | Created locally |
| Argo Rollouts resources | `k8s/apps/prediction-api/base/rollout.yaml` | Created locally |
| Prometheus analysis templates | `k8s/apps/prediction-api/base/analysis-template.yaml` | Created locally |
| Image tag patch | `k8s/apps/prediction-api/overlays/prod/image-tag.yaml` | Created locally |
| Argo CD install notes | `k8s/platform/argocd/install-notes.md` | Filled locally |
| Argo Rollouts install notes | `k8s/platform/argo-rollouts/install-notes.md` | Filled locally |
| Prometheus install notes | `k8s/platform/prometheus/install-notes.md` | Filled locally |
| EFK install notes | `k8s/platform/efk/install-notes.md` | Filled locally |
| General install notes | `docs/install-notes.md` | Filled locally |

The Argo CD source path contains a Kustomize tree that builds locally. Do not build the CD workflow until Terraform defines ECR, EKS, OIDC, and the image tag update path.
