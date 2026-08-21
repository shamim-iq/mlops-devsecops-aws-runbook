# CD Rollout Promotion Rollback Checklist

## CD And GitOps

| Field | Value |
|---|---|
| CD tool | |
| Manual approval mechanism | |
| GitOps repository URL | |
| GitOps branch | |
| Image tag file path | |
| Image tag update method | |
| Argo CD application name | |
| Argo CD sync target | |

## Release Proof

| Item | Value |
|---|---|
| Healthy release image tag | |
| Bad release image tag | |
| Rollout name | |
| Stable service | |
| Canary service | |
| Promotion threshold | |
| Rollback threshold | |

## Evidence

| Evidence | Status |
|---|---|
| Manual approval record | Not captured |
| GitOps image tag change | Not captured |
| Argo CD sync status | Not captured |
| Healthy rollout promotion | Not captured |
| Prometheus healthy analysis | Not captured |
| Bad rollout failure | Not captured |
| Prometheus failed analysis | Not captured |
| Argo Rollouts rollback | Not captured |

Codex must not update GitOps manifests, trigger deployment, run cluster commands, or create Git commits.
