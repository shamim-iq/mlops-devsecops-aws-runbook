# Rollouts Prometheus Analysis Progress

## Current State

`active` - 2026-08-23. Argo Rollouts, Prometheus, Argo CD sync, the real ECR image rollout, the running prediction API pod, and app metrics are verified by owner-run commands. A Prometheus analysis failure aborted a canary, so rollback/block behavior is verified. The implementation chart now needs the request-volume analysis gate merged to `main` and synced for the final successful promotion proof.

## Done

- [x] Record requirement to install Argo Rollouts.
- [x] Record requirement to convert the application deployment to a canary rollout.
- [x] Record requirement to install Prometheus.
- [x] Record required metrics: request count, success/failure rate, and latency.
- [x] Record requirement to configure rollout analysis against Prometheus.
- [x] Record owner-only boundary for live cluster changes.
- [x] Choose Argo Rollouts Helm install in `argo-rollouts`.
- [x] Choose Prometheus Helm install in `monitoring`.
- [x] Record implemented FastAPI metric names.
- [x] Record current canary steps and success threshold.
- [x] Add owner-run install and validation commands.
- [x] Owner installed Argo Rollouts.
- [x] Owner installed Prometheus.
- [x] Owner verified the Helm chart renders in the implementation repository.
- [x] Owner verified Argo CD sync after Rollouts CRDs exist.
- [x] Owner verified the prediction API pod runs from the real ECR image.
- [x] Owner verified `/health`, `/predict`, and `/metrics`.
- [x] Owner verified failed Prometheus analysis aborts the canary.
- [x] Switch final demo analysis gate to request-volume query.

## Remaining

- [ ] Owner commits and merges the request-volume analysis gate to `main`.
- [ ] Owner syncs Argo CD after the final chart change.
- [ ] Owner verifies a successful request-volume `AnalysisRun`.
- [ ] Owner verifies healthy promotion.
