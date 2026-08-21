# CD Rollout Promotion Rollback

This project defines the CD proof for the demo. It covers updating the GitOps image tag after approval, letting Argo CD reconcile the cluster, running a healthy release that promotes, and running a bad release that fails Prometheus analysis and rolls back through Argo Rollouts.

## Owner

Project owner - AWS account kept private, preferred region `us-east-1`.

## Status

`active` - 2026-08-22. The CD, promotion, and rollback scope is recorded. GitOps repository, image tag update method, Argo CD application, rollout analysis thresholds, and evidence capture are not yet finalized.

## Operating Boundary

Codex must not update GitOps manifests, push commits, trigger production deployment, run Kubernetes commands, or modify AWS resources. The owner performs GitOps updates, approvals, sync checks, and rollout validation.

## CD Shape

```text
manual approval
  -> update image tag in GitOps repository
  -> Argo CD detects change
  -> Argo CD reconciles EKS
  -> Argo Rollouts starts canary
  -> Prometheus analysis
  -> promote or rollback
```

The healthy release proves promotion. The bad release proves automatic rollback when Prometheus analysis fails.

> [CONFIRM] GitOps repository URL, image tag update file, CD tool, Argo CD application name, rollout thresholds, healthy release image tag, and bad release image tag are not recorded yet.

## Next

1. Record the approved CD tool and manual approval mechanism.
2. Record the GitOps repository, branch, and image tag file path.
3. Define how CD updates the GitOps image tag after approval.
4. Record the Argo CD application name and sync target.
5. Record healthy release criteria.
6. Record bad release failure behavior.
7. Owner runs a healthy release and verifies Argo Rollouts promotes it.
8. Owner runs a bad release and verifies Prometheus analysis fails it.
9. Owner verifies Argo Rollouts rolls back to the previous stable version.
10. Capture evidence for CI/CD, Argo CD sync, rollout status, Prometheus analysis, and rollback.

## Files

| File | What you'd learn there |
|---|---|
| [Progress.md](./Progress.md) | CD, promotion, rollback, and evidence work completed and remaining |
| [checklist.md](./checklist.md) | GitOps update, Argo CD sync, rollout, rollback, and evidence decisions |
