# CD Rollout Promotion Rollback Progress

## Current State

`complete` - 2026-08-23. The owner completed the CD proof. A healthy image promoted through Argo Rollouts, a forced Prometheus analysis failure aborted the bad rollout, the previous stable ReplicaSet stayed active, evidence was captured, and the GitOps desired state was restored to a healthy image and normal threshold.

## Done

- [x] Record requirement for approved deployment to update GitOps image tag.
- [x] Record requirement for Argo CD reconciliation.
- [x] Record requirement to prove healthy rollout promotion.
- [x] Record requirement to prove failed rollout rollback.
- [x] Record owner-only boundary for GitOps updates, deployment, and cluster validation.
- [x] Record CD tool: GitHub Actions.
- [x] Record manual approval mechanism: GitHub Actions production environment approval.
- [x] Record GitOps repository URL placeholder: `<implementation-repository-url>`.
- [x] Record GitOps branch: `main`.
- [x] Record image tag file path: `k8s/apps/prediction-api/chart/values-prod.yaml`.
- [x] Define image tag update workflow.
- [x] Record Argo CD application name: `prediction-api-prod`.
- [x] Prepare owner commands for healthy promotion and failed rollback proof.
- [x] Record rollout name: `prediction-api`.
- [x] Record healthy release image tag: `demo-20260823-005`.
- [x] Record bad release image tag: `bad-20260823-001`.
- [x] Record Prometheus success threshold: request volume `> 0`.
- [x] Record forced rollback threshold: request volume `> 999999`.
- [x] Owner verified healthy promotion.
- [x] Owner verified failed analysis and rollout abort.
- [x] Owner restored the healthy desired state.
- [x] Owner captured rollout, analysis, pod, and Argo CD evidence.

## Remaining

- [ ] Capture GitHub Actions production approval evidence if required for the final evidence package.
