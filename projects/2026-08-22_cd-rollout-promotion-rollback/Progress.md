# CD Rollout Promotion Rollback Progress

## Current State

`active` - 2026-08-22. The CD proof project is scaffolded. No CD workflow, GitOps update, Argo CD sync, promotion test, or rollback test has been performed.

## Done

- [x] Record requirement for approved deployment to update GitOps image tag.
- [x] Record requirement for Argo CD reconciliation.
- [x] Record requirement to prove healthy rollout promotion.
- [x] Record requirement to prove failed rollout rollback.
- [x] Record owner-only boundary for GitOps updates, deployment, and cluster validation.

## Remaining

- [ ] Record CD tool.
- [ ] Record manual approval mechanism.
- [ ] Record GitOps repository URL.
- [ ] Record GitOps branch.
- [ ] Record image tag file path.
- [ ] Define image tag update command or workflow.
- [ ] Record Argo CD application name.
- [ ] Record rollout name.
- [ ] Record healthy release image tag.
- [ ] Record bad release image tag.
- [ ] Record Prometheus success thresholds.
- [ ] Record Prometheus failure thresholds.
- [ ] Owner verifies healthy promotion.
- [ ] Owner verifies bad release rollback.
- [ ] Capture evidence.
