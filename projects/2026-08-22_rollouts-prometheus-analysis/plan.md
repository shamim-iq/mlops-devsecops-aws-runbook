# Rollouts Prometheus Analysis Plan

This plan pins the progressive delivery decisions for the prediction API. The implementation repository already contains the Helm chart resources, so this project tracks the add-on install choices and the owner-run validation path.

## Add-On Choices

Install Argo Rollouts with the `argo/argo-rollouts` Helm chart into the `argo-rollouts` namespace. This keeps the controller separate from Argo CD and makes CRD ownership clear during cleanup.

Install Prometheus with the `prometheus-community/prometheus` Helm chart into the `monitoring` namespace. Use the in-cluster server URL `http://prometheus-server.monitoring.svc.cluster.local` for Argo Rollouts analysis.

## Application Metrics

The FastAPI app exposes metrics at `GET /metrics`.

| Metric | Meaning |
|---|---|
| `prediction_api_requests_total` | Counter labelled by `endpoint`, `method`, and `status` |
| `prediction_api_prediction_seconds` | Histogram for prediction latency |

The final rollout analysis uses the cumulative request counter because the one-node demo has sparse canary traffic, no traffic router, and short rate windows can return `0` during analysis. The gate proves Prometheus can scrape application metrics before promotion:

```text
sum(prediction_api_requests_total) or vector(0)
```

## Canary Behavior

The prediction API chart renders an Argo Rollouts `Rollout` named `prediction-api` in the `prediction-api` namespace. It starts with one replica, sends 20 percent canary weight, pauses for 60 seconds, runs Prometheus analysis, and promotes to 100 percent if analysis succeeds.

The analysis template is named `prediction-api-request-volume`. It samples every 30 seconds, runs 2 measurements, requires the request counter to be greater than `0`, and allows 1 failed measurement before rollback.

Because the first chart uses one replica and no traffic router, `setWeight` controls the basic canary rollout step instead of exact request-level traffic splitting. Keep it for the one-day demo unless the project adds more replicas and a traffic router later.

## Execution Order

1. Owner confirms the current Kubernetes context is the demo EKS cluster.
2. Owner installs Argo Rollouts and verifies the `Rollout` and `AnalysisTemplate` CRDs exist.
3. Owner installs Prometheus and verifies the server service exists in `monitoring`.
4. Owner renders the prediction API Helm chart with production values.
5. Owner syncs or refreshes the Argo CD application after the add-ons exist.
6. Owner generates healthy prediction traffic during a canary rollout.
7. Owner verifies the rollout promotes.
8. Owner tests rollback with a deliberately bad image tag or failing application change only if cleanup time remains.

## Evidence

Record only non-sensitive status in the evidence project: installed namespaces, CRD names, Prometheus service name, rollout phase, analysis run phase, and whether promotion or rollback occurred. Do not record account IDs, kubeconfig details, tokens, local machine paths, or private repository values.
