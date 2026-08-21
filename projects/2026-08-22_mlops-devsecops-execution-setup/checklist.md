# MLOps DevSecOps Execution Setup Checklist

## Environment

| Field | Value |
|---|---|
| AWS account ID | `447182646004` |
| AWS region | `us-east-1` |
| Codex AWS profile | `codex-read-only` |
| Owner deployment profile | `shamim-mlops-deploy` |
| CI/CD platform | GitHub Actions |
| Source repository | `https://github.com/shamim-iq/mlops-devsecops-aws-runbook.git` |
| Main project directory | `C:\Users\iqbal\OneDrive\Desktop\Prep\MLOps-Project` |
| GitOps repository | Created separate repository: `https://github.com/shamim-iq/mlops-devsecops-aws-gitops.git` |
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
| GitOps manifests | Separate repository | Structure defined, not pushed |

Do not proceed to Terraform planning until source scaffolding exists and the owner confirms the local-state demo choice still fits.
