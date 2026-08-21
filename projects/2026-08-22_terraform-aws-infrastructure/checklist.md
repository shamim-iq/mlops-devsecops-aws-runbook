# Terraform AWS Infrastructure Checklist

## Backend

| Field | Value |
|---|---|
| Backend type | |
| State bucket | |
| Lock table | |
| AWS region | `us-east-1` |
| AWS account ID | `447182646004` |

## Layout

| File or directory | Status |
|---|---|
| `terraform/backend.tf` | Not created |
| `terraform/providers.tf` | Not created |
| `terraform/variables.tf` | Not created |
| `terraform/outputs.tf` | Not created |
| `terraform/main.tf` | Not created |
| `terraform/environments/demo.tfvars` | Not created |
| `terraform/modules/networking/` | Not created |
| `terraform/modules/ecr/` | Not created |
| `terraform/modules/eks/` | Not created |
| `terraform/modules/iam/` | Not created |
| `terraform/modules/secrets/` | Not created |

## Infrastructure

| Area | Required | Status |
|---|---|---|
| Networking | VPC, subnets, routes, security groups | Not defined |
| ECR | Repository and lifecycle/scanning settings | Not defined |
| EKS | Cluster and CPU-only worker capacity | Not defined |
| IAM | Cluster, node, CI/CD, and deployment roles | Not defined |
| OIDC | CI/CD trust and EKS OIDC provider where needed | Not defined |
| Secrets Manager | Runtime or deployment secrets | Not defined |
| Tags | `Project=minimal-mlops-devsecops-pipeline` | Not defined |

## Review Gates

| Gate | Owner |
|---|---|
| `terraform fmt` | Codex or owner |
| `terraform validate` | Codex or owner |
| `terraform plan` | Owner |
| Billable resource review | Owner |
| Permission-sensitive review | Owner |
| `terraform apply` | Owner only |

Codex must not run `terraform apply`, use `shamim-mlops-deploy`, or make AWS resource changes.
