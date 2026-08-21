# MLOps DevSecOps Execution Setup Checklist

## Environment

| Field | Value |
|---|---|
| AWS account ID | `447182646004` |
| AWS region | `us-east-1` |
| Codex AWS profile | `codex-read-only` |
| Owner deployment profile | `shamim-mlops-deploy` |
| CI/CD platform | |
| Source repository | `https://github.com/shamim-iq/mlops-devsecops-aws-runbook.git` |
| GitOps repository | |
| Terraform backend type | |
| Terraform state bucket | |
| Terraform lock table | |

## Cost And Capacity

| Decision | Value |
|---|---|
| GPU allowed | No |
| Cost-control objective | INR 500 |
| EKS control plane cost checked | |
| Candidate worker node type | |
| Worker node count | |
| NAT gateway used | |
| Argo CD included | Yes |
| Argo Rollouts included | Yes |
| Prometheus included | Yes |
| EFK included | Yes, minimal |
| EFK storage limit | |
| EFK retention | |

## Source Repository Structure

| Area | Path | Status |
|---|---|---|
| FastAPI service | `app/` | Not created |
| Model artifact home | `app/model/` | Not created |
| Unit tests | `tests/` | Not created |
| Docker build | `Dockerfile` | Not created |
| Terraform | `terraform/` | Not created |
| CI workflows | `.github/workflows/` | Waiting on CI/CD platform |
| Stable docs | `docs/` | Exists |
| Project tracking | `projects/` | Exists |
| GitOps manifests | Separate repository or folder | Not decided |

Do not proceed to Terraform planning or source scaffolding until the blank environment and cost fields are filled or explicitly deferred.
