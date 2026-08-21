# MLOps DevSecOps Execution Setup Progress

## Current State

`active` - 2026-08-22. The setup project is scaffolded. Known AWS and repository facts are recorded, but deployment platform, Terraform state, and cost choices are still open.

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

## Remaining

- [ ] Record CI/CD platform.
- [ ] Record GitOps repository.
- [ ] Record Terraform state location.
- [ ] Record backend bucket and lock table names if remote state is used.
- [ ] Record current `us-east-1` EKS control plane cost.
- [ ] Record candidate EC2 worker node shapes.
- [ ] Record whether NAT gateway will be avoided for the demo.
- [ ] Record EBS storage size for EFK.
- [ ] Record EFK retention.
- [ ] Pick the final node shape and add-on footprint.
- [ ] Confirm whether GitHub Actions workflow files are needed.
- [ ] Create `app/`.
- [ ] Create `tests/`.
- [ ] Create `terraform/`.
- [ ] Create CI workflow folder after platform choice.
- [ ] Record whether GitOps manifests live in a separate repository.
