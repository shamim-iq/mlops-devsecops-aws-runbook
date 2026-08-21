# Rollouts Prometheus Analysis

This project defines the progressive delivery layer for the demo. It covers installing Argo Rollouts, converting the application deployment to a canary rollout, installing Prometheus, exposing application metrics, and configuring rollout analysis against Prometheus queries.

## Owner

shamim.linkedin@gmail.com - AWS account `447182646004`, preferred region `us-east-1`.

## Status

`active` - 2026-08-22. The rollout and metrics scope is recorded. Argo Rollouts, Prometheus, application metrics, rollout manifests, and analysis templates have not been created.

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

> [CONFIRM] Argo Rollouts install method, Prometheus install method, metric names, scrape path, latency threshold, error-rate threshold, and canary step weights are not finalized yet.

## Next

1. Choose Argo Rollouts install method.
2. Choose Prometheus install method.
3. Define app metric names for request count, success count, failure count, and latency.
4. Expose metrics from the FastAPI app.
5. Define Prometheus scrape configuration.
6. Convert the application Deployment to an Argo Rollout.
7. Define canary steps and traffic percentages.
8. Create Argo Rollouts `AnalysisTemplate` queries against Prometheus.
9. Owner installs Argo Rollouts and Prometheus.
10. Owner verifies a healthy rollout promotes.
11. Owner verifies a failing rollout rolls back.

## Files

| File | What you'd learn there |
|---|---|
| [Progress.md](./Progress.md) | Rollout, Prometheus, metrics, and analysis work completed and remaining |
| [checklist.md](./checklist.md) | Add-on, metric, canary, and Prometheus analysis decisions |
