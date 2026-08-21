# Rollouts Prometheus Analysis Progress

## Current State

`active` - 2026-08-22. The rollouts and Prometheus analysis project is scaffolded. No cluster add-ons or rollout resources have been installed.

## Done

- [x] Record requirement to install Argo Rollouts.
- [x] Record requirement to convert the application deployment to a canary rollout.
- [x] Record requirement to install Prometheus.
- [x] Record required metrics: request count, success/failure rate, and latency.
- [x] Record requirement to configure rollout analysis against Prometheus.
- [x] Record owner-only boundary for live cluster changes.

## Remaining

- [ ] Choose Argo Rollouts install method.
- [ ] Choose Prometheus install method.
- [ ] Define request count metric.
- [ ] Define success rate or success count metric.
- [ ] Define failure rate or failure count metric.
- [ ] Define latency metric.
- [ ] Define Prometheus scrape path.
- [ ] Define canary step weights.
- [ ] Define success threshold.
- [ ] Define failure threshold.
- [ ] Create Rollout manifest.
- [ ] Create Prometheus `AnalysisTemplate`.
- [ ] Owner installs Argo Rollouts.
- [ ] Owner installs Prometheus.
- [ ] Owner verifies healthy promotion.
- [ ] Owner verifies failed rollout rollback.
