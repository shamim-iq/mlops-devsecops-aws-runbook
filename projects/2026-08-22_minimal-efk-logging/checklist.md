# Minimal EFK Logging Checklist

## Helm

| Component | Chart | Version | Namespace | Status |
|---|---|---|---|---|
| Elasticsearch | | | | Not selected |
| Fluent Bit | | | | Not selected |
| Kibana | | | | Not selected |

## Cost Controls

| Setting | Value |
|---|---|
| Elasticsearch replica count | |
| Elasticsearch storage size | |
| Log retention | |
| Index cleanup method | |
| CPU requests | |
| Memory requests | |

## Access And Verification

| Item | Value |
|---|---|
| Kibana access method | |
| Log source namespace | |
| Application log query | |
| Verification evidence | |
| Cleanup command location | |

Codex must not install Helm charts or modify EKS logging resources.
