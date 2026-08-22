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
| Networking | VPC, subnets, routes, security groups | Defined, applied, verified |
| ECR | Repository and lifecycle/scanning settings | Defined, applied, verified |
| EKS | Cluster and CPU-only worker capacity | Defined, applied, verified |
| IAM | Cluster, node, CI/CD, and deployment roles | Defined, applied, verified |
| OIDC | CI/CD trust and EKS OIDC provider where needed | Defined, applied, verified |
| Secrets Manager | Runtime or deployment secrets | Defined, applied, verified |
| Tags | `Project=minimal-mlops-devsecops-pipeline` | Applied and verified |

## Review Gates

| Gate | Owner |
|---|---|
| `terraform fmt` | Codex or owner |
| `terraform validate` | Codex or owner |
| `terraform init -backend=false` | Codex or owner |
| `terraform plan` | Owner - complete |
| Billable resource review | Owner - complete |
| Permission-sensitive review | Owner - complete |
| `terraform apply` | Owner only - complete |

## Closeout

| Item | Status |
|---|---|
| Read-only AWS verification | Complete |
| Final no-drift Terraform plan | Complete |
| Implementation repository commit and push | Pending owner |
| Pull request evidence update | Pending owner |
| Demo cleanup | Pending after demonstration |

Codex must not run `terraform apply`, use `<deployment-aws-profile>`, or make AWS resource changes.
