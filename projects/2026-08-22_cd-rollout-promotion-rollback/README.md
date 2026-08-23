# CD Rollout Promotion Rollback

This project defines the CD proof for the demo. It covers updating the GitOps image tag after approval, letting Argo CD reconcile the cluster, running a healthy release that promotes, and running a bad release that fails Prometheus analysis and rolls back through Argo Rollouts.

## Owner

Project owner - AWS account kept private, preferred region `us-east-1`.

## Status

`complete` - 2026-08-23. The owner proved the CD path with GitOps commits, Argo CD sync, Argo Rollouts canary promotion, forced Prometheus analysis failure, rollout abort, rollback to the prior stable ReplicaSet, and final restore to a healthy desired state. The final application state is `Synced` and `Healthy`.

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

## CD Execution Model

GitHub Actions performs CD only after the production environment approval passes. The approved deployment updates the production Helm values file, commits the image tag change to the GitOps branch, and leaves Argo CD to reconcile the desired state into EKS.

The image tag update target is `image.tag` in `k8s/apps/prediction-api/chart/values-prod.yaml`. The GitOps branch is `main`. The Argo CD application name is `prediction-api-prod`, with source path `k8s/apps/prediction-api/chart`.

## What Was Done

The healthy release used image tag `demo-20260823-005`. Argo CD synced the GitOps commit, Argo Rollouts completed all four canary steps, Prometheus analysis succeeded, and the rollout became `Healthy`.

The first bad release with image tag `bad-20260823-001` promoted because the analysis query measured global request volume, which still included prior healthy traffic. The owner then restored the healthy baseline and reran the bad release with a deliberately unreachable request-volume threshold. Prometheus analysis failed, Argo Rollouts aborted the update, kept stable ReplicaSet `6cf6768455`, and Argo CD reported `Synced` and `Degraded` during the failed proof.

The owner restored `demo-20260823-005` and the normal request-volume threshold after collecting evidence. Argo CD then synced the restore commit, and the application returned to `Synced` and `Healthy`.

## Next

1. Capture the GitHub Actions production environment approval record if it is needed for the final evidence package.
2. Move to evidence and cleanup once the remaining project proofs are complete.

## Files

| File | What you'd learn there |
|---|---|
| [Progress.md](./Progress.md) | CD, promotion, rollback, and evidence work completed and remaining |
| [checklist.md](./checklist.md) | GitOps update, Argo CD sync, rollout, rollback, and evidence decisions |
| [owner-commands.md](./owner-commands.md) | Owner-run commands for healthy promotion and failed rollback proof |
