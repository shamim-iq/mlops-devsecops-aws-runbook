# GitOps Repository Structure Checklist

## Repository

| Field | Value |
|---|---|
| GitOps repository URL | |
| Default branch | |
| Repository model | Separate repository or source repository folder |
| Argo CD source path | |
| Environment layout | |

## Required Structure

| Area | Path | Status |
|---|---|---|
| Prediction API base manifests | `apps/prediction-api/base/` | Not created |
| Production overlay | `apps/prediction-api/overlays/prod/` | Not created |
| Argo Rollouts resources | `rollouts/prediction-api/` | Not created |
| Prometheus analysis templates | `analysis/prometheus/` | Not created |
| Argo CD install notes | `platform/argocd/` | Not created |
| Argo Rollouts install notes | `platform/argo-rollouts/` | Not created |
| Prometheus install notes | `platform/prometheus/` | Not created |
| EFK install notes | `platform/efk/` | Not created |
| General install notes | `docs/install-notes.md` | Not created |

Do not build the CD workflow until the GitOps repository URL, branch, and Argo CD source path are recorded.
