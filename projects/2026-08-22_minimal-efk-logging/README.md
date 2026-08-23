# Minimal EFK Logging

This project defines the minimal EFK logging layer for the demo EKS cluster. It covers Helm-based installation notes for Elasticsearch, Fluent Bit, and Kibana, with retention and storage limits kept small so logging does not dominate the cost objective.

## Owner

Project owner - AWS account kept private, preferred region `us-east-1`.

## Status

`complete` - 2026-08-23. The owner installed the minimal EFK stack, applied one-day retention, verified `prediction-api` namespace logs in Elasticsearch, and confirmed Elasticsearch, Kibana, and Fluent Bit run together after temporarily scaling the node group to two nodes. Codex did not install Helm charts or change live EKS logging resources.

## Operating Boundary

Codex must not install Helm charts, run Kubernetes commands against EKS, or change live logging resources. The owner performs Helm installs and cluster changes with approved deployment access.

## Logging Shape

```text
application and Kubernetes logs
  -> Fluent Bit DaemonSet
  -> Elasticsearch
  -> Kibana
```

EFK is for demo evidence and short-term troubleshooting only. Elasticsearch uses one multi-role pod with ephemeral demo storage, Kibana runs as the bundled Bitnami subchart, and Fluent Bit runs as the official collector DaemonSet. Logs are scoped to the `prediction-api` namespace and indexed as `prediction-api-logs*`, with Index Lifecycle Management deleting matching indices after one day. The original single-node cluster hit its pod limit, so the owner temporarily scaled the node group to two nodes to run Elasticsearch, Kibana, and Fluent Bit at the same time.

## Next

1. Owner verifies the `prediction-api-logs*` data view in Kibana Discover.
2. Owner records non-sensitive EFK evidence.
3. Owner removes EFK resources during cleanup.
4. Owner scales the node group back down during cleanup.

## Files

| File | What you'd learn there |
|---|---|
| [Progress.md](./Progress.md) | EFK logging work completed and remaining |
| [checklist.md](./checklist.md) | Helm chart, retention, storage, and access decisions |
| [owner-commands.md](./owner-commands.md) | Owner-run install, verification, evidence, and cleanup commands |
| [values-elasticsearch-kibana-demo.yaml](./values-elasticsearch-kibana-demo.yaml) | Minimal Elasticsearch and bundled Kibana Helm values |
| [values-fluent-bit-collector-demo.yaml](./values-fluent-bit-collector-demo.yaml) | Minimal Fluent Bit collector Helm values |
