# Rollouts Prometheus Analysis Checklist

## Add-Ons

| Item | Value |
|---|---|
| Argo Rollouts install method | |
| Argo Rollouts namespace | |
| Prometheus install method | |
| Prometheus namespace | |
| Prometheus service URL | |

## Application Metrics

| Metric | Name | Status |
|---|---|---|
| Request count | | Not defined |
| Success count or rate | | Not defined |
| Failure count or rate | | Not defined |
| Latency | | Not defined |
| Metrics endpoint | `GET /metrics` | Not implemented |

## Canary Rollout

| Field | Value |
|---|---|
| Rollout name | |
| Stable service | |
| Canary service | |
| Canary steps | |
| Promotion condition | |
| Rollback condition | |

## Prometheus Analysis

| Query | Purpose | Status |
|---|---|---|
| Request volume query | Ensure enough traffic for analysis | Not defined |
| Success rate query | Promote healthy release | Not defined |
| Failure rate query | Detect bad release | Not defined |
| Latency query | Detect slow release | Not defined |

Codex must not install cluster add-ons or apply rollout resources to EKS.
