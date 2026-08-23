# Rollouts Prometheus Analysis Checklist

## Add-Ons

| Item | Value |
|---|---|
| Argo Rollouts install method | Helm chart `argo/argo-rollouts` |
| Argo Rollouts namespace | `argo-rollouts` |
| Prometheus install method | Helm chart `prometheus-community/prometheus` |
| Prometheus namespace | `monitoring` |
| Prometheus service URL | `http://prometheus-server.monitoring.svc.cluster.local` |

## Application Metrics

| Metric | Name | Status |
|---|---|---|
| Request count | `prediction_api_requests_total` | Implemented locally |
| Success count or rate | `prediction_api_requests_total{status="200"}` | Exposed, not gated in final demo |
| Failure count or rate | Non-`200` slice of `prediction_api_requests_total` | Available from labels |
| Latency | `prediction_api_prediction_seconds` | Exposed, not gated |
| Metrics endpoint | `GET /metrics` | Implemented locally |

## Canary Rollout

| Field | Value |
|---|---|
| Rollout name | `prediction-api` |
| Stable service | `prediction-api` |
| Canary service | Not separate in the first chart |
| Canary steps | Basic canary `20%`, pause `60s`, run analysis, then `100%` |
| Promotion condition | Prometheus request counter is greater than `0` |
| Rollback condition | Analysis reaches failure limit |

## Prometheus Analysis

| Query | Purpose | Status |
|---|---|---|
| Request volume query | Ensure Prometheus sees app request metrics | Implemented in final gate |
| Success rate query | Promote healthy release | Replaced by request-volume gate for demo stability |
| Failure rate query | Detect bad release | Failed analysis abort verified |
| Latency query | Detect slow release | Metric exists, not implemented in first gate |

Codex must not install cluster add-ons or apply rollout resources to EKS.
