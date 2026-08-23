# Minimal EFK Logging Checklist

## Helm

| Component | Chart | Version | Namespace | Status |
|---|---|---|---|---|
| Elasticsearch | `oci://registry-1.docker.io/bitnamicharts/elasticsearch` | `22.1.6` | `logging` | Deployed |
| Fluent Bit | `oci://ghcr.io/fluent/helm-charts/fluent-bit-collector` | `1.1.1` | `logging` | Deployed |
| Kibana | Bundled Bitnami Elasticsearch subchart | `12.x.x` via Elasticsearch chart | `logging` | Deployed |

## Cost Controls

| Setting | Value |
|---|---|
| Elasticsearch replica count | One multi-role master pod; data, coordinating, and ingest-only pods disabled |
| Elasticsearch storage size | Ephemeral pod storage for the demo; no PVC |
| Log retention | Delete matching indices after `1d` |
| Index cleanup method | Elasticsearch Index Lifecycle Management policy plus index template |
| CPU requests | Elasticsearch `250m`, Kibana `100m`, Fluent Bit `25m` |
| Memory requests | Elasticsearch `768Mi`, Kibana `512Mi`, Fluent Bit `64Mi` |

## Access And Verification

| Item | Value |
|---|---|
| Kibana access method | Temporary `kubectl port-forward` to `svc/elasticsearch-kibana` |
| Log source namespace | `prediction-api` |
| Application log query | `kubernetes.namespace_name:prediction-api` against `prediction-api-logs*` |
| Verification evidence | Elasticsearch returned `prediction-api` namespace hits in `prediction-api-logs`; Kibana data view verification remains to capture |
| Cleanup command location | [owner-commands.md](./owner-commands.md) |
| Capacity note | Node group temporarily scaled to two nodes so Elasticsearch, Kibana, and Fluent Bit run together |

Codex must not install Helm charts or modify EKS logging resources.
