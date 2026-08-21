# MLOps DevSecOps Execution Setup Progress

## Current State

`active` - 2026-08-22. Execution setup decisions are recorded, the GitOps repository exists, and the initial source scaffold exists in `C:\Users\iqbal\OneDrive\Desktop\Prep\MLOps-Project`. No AWS resources have been deployed or changed.

## Done

- [x] Record AWS account ID: `447182646004`.
- [x] Record preferred AWS region: `us-east-1`.
- [x] Record source repository: `https://github.com/shamim-iq/mlops-devsecops-aws-runbook.git`.
- [x] Record that Codex is limited to `codex-read-only`.
- [x] Record that only the owner uses `shamim-mlops-deploy`.
- [x] Record CPU-only constraint.
- [x] Record INR 500 as a cost-control objective, not a guaranteed billing ceiling.
- [x] Record required add-ons: Argo CD, Argo Rollouts, Prometheus, and minimal EFK.
- [x] Record required repository areas: FastAPI app, Docker build, tests, CI workflow, Terraform, and docs.
- [x] Record CI/CD platform: GitHub Actions.
- [x] Record GitOps repository approach: separate repository.
- [x] Record Terraform state location: local state for demo.
- [x] Record current `us-east-1` EKS control plane cost: USD 0.10 per cluster-hour.
- [x] Record candidate EC2 worker node shape: one `t3.medium`.
- [x] Record NAT Gateway choice: avoid NAT Gateway.
- [x] Record EFK storage candidate: 8 GiB gp3.
- [x] Record EFK retention: 1 day.
- [x] Confirm GitOps repository exists: `https://github.com/shamim-iq/mlops-devsecops-aws-gitops.git`.
- [x] Define the initial GitOps repository structure.
- [x] Create `app/model/` in the main project directory.
- [x] Create `tests/` in the main project directory.
- [x] Create `terraform/` in the main project directory.
- [x] Create `.github/workflows/` in the main project directory.
- [x] Create `docs/` in the main project directory.

## Remaining

- [ ] Push the initial GitOps repository structure.
- [ ] Re-check the `t3.medium` candidate after Helm resource requests are defined.
- [ ] Confirm whether local Terraform state remains acceptable before Terraform work starts.
- [ ] Add the FastAPI service skeleton.
- [ ] Add the first unit tests.
- [ ] Add Terraform provider, variables, and backend files.
- [ ] Add the first GitHub Actions workflow after app commands exist.
