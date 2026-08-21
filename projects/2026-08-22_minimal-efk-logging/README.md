# Minimal EFK Logging

This project defines the minimal EFK logging layer for the demo EKS cluster. It covers Helm-based installation notes for Elasticsearch, Fluent Bit, and Kibana, with retention and storage limits kept small so logging does not dominate the cost objective.

## Owner

Project owner - AWS account kept private, preferred region `us-east-1`.

## Status

`active` - 2026-08-22. The minimal EFK logging scope is recorded. Helm chart choices, namespaces, storage size, retention, and install values are not yet finalized.

## Operating Boundary

Codex must not install Helm charts, run Kubernetes commands against EKS, or change live logging resources. The owner performs Helm installs and cluster changes with approved deployment access.

## Logging Shape

```text
application and Kubernetes logs
  -> Fluent Bit DaemonSet
  -> Elasticsearch
  -> Kibana
```

EFK is for demo evidence and short-term troubleshooting only. Retention, replicas, storage, and resource requests must stay minimal.

> [CONFIRM] Helm chart names, chart versions, namespace, Elasticsearch storage size, retention policy, Kibana access method, and resource limits are not recorded yet.

## Next

1. Choose Helm charts and versions for Elasticsearch, Fluent Bit, and Kibana.
2. Record the logging namespace.
3. Set Elasticsearch storage size and replica count.
4. Set log retention or index cleanup approach.
5. Set CPU and memory requests for the logging components.
6. Decide Kibana access method for the demo.
7. Owner installs EFK with Helm.
8. Owner verifies application logs appear in Kibana.
9. Owner records cleanup commands for EFK resources.

## Files

| File | What you'd learn there |
|---|---|
| [Progress.md](./Progress.md) | EFK logging work completed and remaining |
| [checklist.md](./checklist.md) | Helm chart, retention, storage, and access decisions |
