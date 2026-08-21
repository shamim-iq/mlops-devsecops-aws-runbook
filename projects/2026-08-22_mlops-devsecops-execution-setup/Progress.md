# MLOps DevSecOps Execution Setup Progress

## Current State

`active` - 2026-08-22. Execution setup decisions are recorded, the implementation repository exists, and the initial single-repository scaffold is pushed to `main` at commit `18518cf`. No AWS resources have been deployed or changed.

## Done

- [x] Record that the AWS account ID is private and not committed.
- [x] Record preferred AWS region: `us-east-1`.
- [x] Record runbook repository: `<runbook-repository-url>`.
- [x] Record implementation repository: `<implementation-repository-url>`.
- [x] Record that Codex is limited to `<read-only-aws-profile>`.
- [x] Record that only the owner uses `<deployment-aws-profile>`.
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
- [x] Confirm implementation repository exists: `<implementation-repository-url>`.
- [x] Define the initial single-repository structure.
- [x] Create local `k8s/` folders for Kubernetes desired state.
- [x] Create `app/model/` in the main project directory.
- [x] Create `tests/` in the main project directory.
- [x] Create `terraform/` in the main project directory.
- [x] Create `.github/workflows/` in the main project directory.
- [x] Create `docs/` in the main project directory.
- [x] Add placeholder files so Git tracks the initial structure.
- [x] Push the initial single-repository structure.
- [x] Add the FastAPI service skeleton.
- [x] Add the first unit tests.

## Remaining

- [ ] Re-check the `t3.medium` candidate after Helm resource requests are defined.
- [ ] Confirm whether local Terraform state remains acceptable before Terraform work starts.
- [ ] Add Terraform provider, variables, and backend files.
- [ ] Add the first GitHub Actions workflow after app commands exist.
