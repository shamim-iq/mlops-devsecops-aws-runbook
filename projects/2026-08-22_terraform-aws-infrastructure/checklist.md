# Terraform AWS Infrastructure Checklist

## Backend

| Field | Value |
|---|---|
| Backend type | Local state for initial demo scaffold |
| State bucket | Not used |
| Lock table | Not used |
| AWS region | `us-east-1` |
| AWS account ID | Private, not committed |

## Layout

| File or directory | Status |
|---|---|
| `terraform/backend.tf` | Created |
| `terraform/providers.tf` | Created |
| `terraform/variables.tf` | Created |
| `terraform/outputs.tf` | Created |
| `terraform/main.tf` | Created |
| `terraform/versions.tf` | Created |
| `terraform/envs/prod/demo.tfvars.example` | Created |
| `terraform/modules/networking/` | Interface created |
| `terraform/modules/ecr/` | Interface created |
| `terraform/modules/eks/` | Interface created |
| `terraform/modules/iam/` | Interface created |
| `terraform/modules/secrets/` | Interface created |

## Infrastructure

| Area | Required | Status |
|---|---|---|
| Networking | VPC, subnets, routes, security groups | Not defined |
| ECR | Repository and lifecycle/scanning settings | Not defined |
| EKS | Cluster and CPU-only worker capacity | Not defined |
| IAM | Cluster, node, CI/CD, and deployment roles | Not defined |
| OIDC | CI/CD trust and EKS OIDC provider where needed | Not defined |
| Secrets Manager | Runtime or deployment secrets | Not defined |
| Tags | `Project=minimal-mlops-devsecops-pipeline` | Defined in variables |

## Review Gates

| Gate | Owner |
|---|---|
| `terraform fmt` | Codex or owner |
| `terraform validate` | Codex or owner |
| `terraform init -backend=false` | Codex or owner |
| `terraform plan` | Owner |
| Billable resource review | Owner |
| Permission-sensitive review | Owner |
| `terraform apply` | Owner only |

Codex must not run `terraform apply`, use `<deployment-aws-profile>`, or make AWS resource changes.
