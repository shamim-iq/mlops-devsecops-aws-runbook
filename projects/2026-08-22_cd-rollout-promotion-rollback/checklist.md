# CD Rollout Promotion Rollback Checklist

## CD And GitOps

| Field | Value |
|---|---|
| CD tool | GitHub Actions |
| Manual approval mechanism | GitHub Actions production environment approval |
| GitOps repository URL | `<implementation-repository-url>` |
| GitOps branch | `main` |
| Image tag file path | `k8s/apps/prediction-api/chart/values-prod.yaml` |
| Image tag update method | Update `image.tag` after approval, then commit the GitOps values change |
| Argo CD application name | `prediction-api-prod` |
| Argo CD sync target | `k8s/apps/prediction-api/chart` rendered with `values-prod.yaml` |

## Release Proof

| Item | Value |
|---|---|
| Healthy release image tag | `demo-20260823-005` |
| Bad release image tag | `bad-20260823-001` |
| Rollout name | `prediction-api` |
| Stable service | `prediction-api` |
| Canary service | Not configured; canary used ReplicaSet weight without a separate canary service |
| Promotion threshold | Request volume `> 0` |
| Rollback threshold | Forced proof threshold `> 999999` with `failureLimit: 1` |

## Evidence

| Evidence | Status |
|---|---|
| Manual approval record | Not captured |
| GitOps image tag change | Captured in GitOps commits |
| Argo CD sync status | Captured |
| Healthy rollout promotion | Captured |
| Prometheus healthy analysis | Captured |
| Bad rollout failure | Captured |
| Prometheus failed analysis | Captured |
| Argo Rollouts rollback | Captured |
| Final restore to healthy state | Captured |

Codex must not update GitOps manifests, trigger deployment, run cluster commands, or create Git commits.
