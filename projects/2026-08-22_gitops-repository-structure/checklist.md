# GitOps Repository Structure Checklist

## Repository

| Field | Value |
|---|---|
| GitOps repository URL | `https://github.com/shamim-iq/mlops-devsecops-aws-gitops.git` |
| Default branch | `main` |
| Repository model | Separate repository |
| Argo CD source path | `apps/prediction-api/overlays/prod` |
| Environment layout | `prod` only for the demo |

## Required Structure

| Area | Path | Status |
|---|---|---|
| Prediction API base manifests | `apps/prediction-api/base/` | Defined, not pushed |
| Production overlay | `apps/prediction-api/overlays/prod/` | Defined, not pushed |
| Argo Rollouts resources | `apps/prediction-api/base/rollout.yaml` | Defined, not pushed |
| Prometheus analysis templates | `apps/prediction-api/base/analysis-template.yaml` | Defined, not pushed |
| Argo CD install notes | `platform/argocd/install-notes.md` | Defined, not pushed |
| Argo Rollouts install notes | `platform/argo-rollouts/install-notes.md` | Defined, not pushed |
| Prometheus install notes | `platform/prometheus/install-notes.md` | Defined, not pushed |
| EFK install notes | `platform/efk/install-notes.md` | Defined, not pushed |
| General install notes | `docs/install-notes.md` | Defined, not pushed |

Do not build the CD workflow until the initial GitOps structure is pushed and the Argo CD source path exists on `main`.
