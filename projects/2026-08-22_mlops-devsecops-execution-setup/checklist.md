# MLOps DevSecOps Execution Setup Checklist

## Environment

| Field | Value |
|---|---|
| AWS account ID | Private, not committed |
| AWS region | `us-east-1` |
| Codex AWS profile | `<read-only-aws-profile>` |
| Owner deployment profile | `<deployment-aws-profile>` |
| CI/CD platform | GitHub Actions |
| Runbook repository | `<runbook-repository-url>` |
| Implementation repository | `<implementation-repository-url>` |
| Main project directory | `<local-implementation-repo>` |
| Repository model | Single repository for app, Terraform, CI, docs, and Kubernetes desired state |
| Terraform backend type | Local state for demo |
| Terraform state bucket | Not used |
| Terraform lock table | Not used |

## Cost And Capacity

| Decision | Value |
|---|---|
| GPU allowed | No |
| Cost-control objective | INR 500 |
| EKS control plane cost checked | Verified 2026-08-22: USD 0.10 per cluster-hour for standard support |
| Candidate worker node type | `t3.medium` |
| Worker node count | 1 |
| NAT gateway used | No |
| Argo CD included | Yes |
| Argo Rollouts included | Yes |
| Prometheus included | Yes |
| EFK included | Yes, minimal |
| EFK storage limit | 8 GiB gp3 candidate |
| EFK retention | 1 day |

## Source Repository Structure

| Area | Path | Status |
|---|---|---|
| FastAPI service | `app/` | Created in main project directory |
| Model artifact home | `app/model/` | Created in main project directory |
| Unit tests | `tests/` | Created in main project directory |
| Docker build | `Dockerfile` | Deferred to model API project |
| Terraform | `terraform/` | Created in main project directory |
| CI workflows | `.github/workflows/` | Created in main project directory |
| Stable docs | `docs/` | Exists |
| Project tracking | `projects/` | Exists |
| Kubernetes desired state | `k8s/` | Placeholder structure pushed |

Do not proceed to Terraform planning until source scaffolding exists and the owner confirms the local-state demo choice still fits.
