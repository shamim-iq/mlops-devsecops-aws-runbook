# CI Access And Approval Pipeline Checklist

## Access

| Field | Value |
|---|---|
| AWS account ID | Private, not committed |
| AWS region | `us-east-1` |
| Codex AWS profile | `<read-only-aws-profile>` |
| Owner deployment profile | `<deployment-aws-profile>` |
| CI/CD platform | |
| Pipeline OIDC provider | |
| Pipeline IAM role | |
| ECR repository | |
| EKS cluster | |

## CI Steps

| Step | Tool or command | Status |
|---|---|---|
| Checkout | | Not defined |
| Install dependencies | | Not defined |
| Unit tests | | Not defined |
| Linting | | Not defined |
| SAST | | Not defined |
| SCA | | Not defined |
| Secrets scan | | Not defined |
| Terraform fmt | `terraform fmt -check` | Not defined |
| Terraform validate | `terraform validate` | Not defined |
| Terraform plan check | Owner-approved mode needed | Not defined |
| Docker build | | Not defined |
| Trivy image scan | | Not defined |
| ECR push | Owner/pipeline only | Not defined |
| Manual approval | | Not defined |

## Gates

| Gate | Required outcome |
|---|---|
| Tests | Pass |
| Linting | Pass |
| SAST | Below configured threshold |
| SCA | Below configured threshold |
| Secrets scan | No committed secrets |
| Terraform checks | Format, validate, and plan check pass |
| Trivy | Below configured threshold |
| Approval | Owner approves before production deployment |

Codex must not run the ECR push, assume deployment roles, or configure production deployment.
