# Rollouts Prometheus Analysis

This project defines the progressive delivery layer for the demo. It covers installing Argo Rollouts, converting the application deployment to a canary rollout, installing Prometheus, exposing application metrics, and configuring rollout analysis against Prometheus queries.

## Owner

Project owner - AWS account kept private, preferred region `us-east-1`.

## Status

`active` - 2026-08-23. Argo Rollouts, Prometheus, Argo CD sync, the real ECR image rollout, the running prediction API pod, `/health`, `/predict`, and `/metrics` are verified. A failed Prometheus analysis aborted a canary, which proves the rollback/block path. The final chart change switches the demo gate from success-rate ratio to request-volume so the next canary can prove successful promotion.

## Operating Boundary

Codex must not install cluster add-ons, run Kubernetes commands against EKS, or change live workloads. The owner performs cluster changes and validates rollout behavior with approved deployment access.

## Delivery Shape

```text
FastAPI metrics endpoint
  -> Prometheus scrape
  -> Argo Rollouts AnalysisTemplate
  -> canary analysis
  -> promote or rollback
```

The app must expose request count, success/failure rate, and latency metrics before rollout analysis can be meaningful. Argo Rollouts should promote only when Prometheus analysis succeeds.

The current chart uses Helm, deploys the app as an Argo Rollouts `Rollout`, scrapes `GET /metrics`, and gates promotion with a Prometheus request-volume query against `prediction_api_requests_total`. The app also exposes `prediction_api_prediction_seconds`, but latency is not part of the first analysis gate.

> [CONFIRM] Successful promotion through the final request-volume AnalysisRun is not verified yet.

## Next

1. Owner commits and merges the request-volume `AnalysisTemplate` chart change to `main`.
2. Owner syncs or refreshes the Argo CD application.
3. Owner triggers one final image-tag rollout.
4. Owner generates prediction traffic during the canary pause.
5. Owner verifies a successful `AnalysisRun` and healthy promoted rollout.

## Files

| File | What you'd learn there |
|---|---|
| [Progress.md](./Progress.md) | Rollout, Prometheus, metrics, and analysis work completed and remaining |
| [checklist.md](./checklist.md) | Add-on, metric, canary, and Prometheus analysis decisions |
| [plan.md](./plan.md) | Add-on choices, metric names, canary behavior, and evidence path |
| [owner-commands.md](./owner-commands.md) | Exact owner-run PowerShell commands for add-on install and rollout validation |
