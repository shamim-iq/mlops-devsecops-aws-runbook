# MLOps DevSecOps Execution Setup

This project prepares the execution inputs for the minimal MLOps DevSecOps pipeline before implementation starts. It records the AWS and repository facts, checks the EKS cost and capacity choices, and defines the source repository structure for the FastAPI service, Docker build, tests, CI workflow, Terraform, and docs.

## Owner

shamim.linkedin@gmail.com - AWS account `447182646004`, preferred region `us-east-1`.

## Status

`active` - 2026-08-22. AWS account, preferred region, source repository, and AWS profile boundaries are recorded. CI/CD platform, GitOps repository, Terraform state location, EKS node shape, and logging retention are not yet recorded.

## Setup Scope

This setup project covers the first three execution steps from [docs/plan.md](../../docs/plan.md). It does not deploy AWS resources and does not create Git history. Codex remains limited to the `codex-read-only` AWS profile for inspection only.

| Area | Current state |
|---|---|
| AWS account | `447182646004` |
| AWS region | `us-east-1` |
| Codex AWS profile | `codex-read-only` |
| Owner deployment profile | `shamim-mlops-deploy` |
| Source repository | `https://github.com/shamim-iq/mlops-devsecops-aws-runbook.git` |
| CI/CD platform | Not recorded |
| GitOps repository | Not recorded |
| Terraform state location | Not recorded |
| EKS node shape | Not recorded |
| Logging retention | Not recorded |

> [CONFIRM] CI/CD platform, GitOps repository, Terraform state location, EKS node shape, current AWS pricing, and logging retention are not recorded yet.

## Next

1. Record the CI/CD platform.
2. Decide whether GitOps uses a separate repository.
3. Choose local Terraform state or remote S3 plus DynamoDB state locking.
4. Confirm current `us-east-1` EKS, EC2, EBS, NAT, and log storage costs.
5. Select the smallest CPU-only EKS node shape that can run Argo CD, Argo Rollouts, Prometheus, minimal EFK, and the FastAPI service.
6. Decide EFK storage and retention limits.
7. Approve the source repository structure before creating application, test, CI, and Terraform folders.

## Files

| File | What you'd learn there |
|---|---|
| [Progress.md](./Progress.md) | What setup work is done and what still blocks implementation |
| [checklist.md](./checklist.md) | Fields and decisions to fill before source and Terraform scaffolding |
