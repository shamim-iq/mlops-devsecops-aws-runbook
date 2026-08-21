# MLOps DevSecOps Execution Setup

This project prepares the execution inputs for the minimal MLOps DevSecOps pipeline before implementation starts. It records the AWS and repository facts, checks the EKS cost and capacity choices, and defines the single implementation repository structure for the FastAPI service, Docker build, tests, CI workflow, Terraform, Kubernetes desired state, and docs.

## Owner

Project owner - AWS account kept private, preferred region `us-east-1`.

## Status

`active` - 2026-08-22. AWS account, preferred region, implementation repository, AWS profile boundaries, CI/CD platform, Terraform state approach, EKS node candidate, NAT choice, and logging retention are recorded. The initial implementation scaffold is pushed to `main` at commit `18518cf`.

## Setup Scope

This setup project covers the first three execution steps from [docs/plan.md](../../docs/plan.md). It does not deploy AWS resources and does not create Git history. Codex remains limited to the `<read-only-aws-profile>` AWS profile for inspection only.

| Area | Current state |
|---|---|
| AWS account | Private, not committed |
| AWS region | `us-east-1` |
| Codex AWS profile | `<read-only-aws-profile>` |
| Owner deployment profile | `<deployment-aws-profile>` |
| Runbook repository | `<runbook-repository-url>` |
| Implementation repository | `<implementation-repository-url>` |
| Main project directory | `<local-implementation-repo>` |
| CI/CD platform | GitHub Actions |
| Repository model | Single repository for app, Terraform, CI, docs, and Kubernetes desired state |
| Terraform state location | Local state for the one-day demo |
| EKS node shape | One CPU-only `t3.medium` worker candidate |
| Logging retention | Minimal EFK retention: 1 day |

Cost check verified 2026-08-22 from AWS pricing pages for [EKS](https://aws.amazon.com/eks/pricing/), [EC2 T3](https://aws.amazon.com/ec2/instance-types/t3/), [VPC NAT Gateway](https://aws.amazon.com/vpc/pricing/), and [EBS](https://aws.amazon.com/ebs/pricing/). In `us-east-1`, standard-support EKS control plane pricing is USD 0.10 per cluster-hour. A 24-hour cluster run costs about USD 2.40 before worker nodes, storage, IPv4, data transfer, and logs. Using a recent USD/INR reference rate around 95.7 means the INR 500 objective is about USD 5.22, so the demo must keep the cluster short-lived. One `t3.medium` Linux worker is USD 0.0418 per hour. NAT Gateway is avoided because one NAT Gateway is USD 0.045 per hour plus USD 0.045 per GB processed. EBS `gp3` storage is USD 0.08 per GB-month, so EFK storage stays at 8 GiB with 1-day retention.

## Next

1. Add the FastAPI model-serving skeleton in the main project directory.
2. Re-check the selected `t3.medium` footprint after Helm chart resource requests are defined.
3. Keep all AWS apply, deploy, and delete commands owner-run with `<deployment-aws-profile>`.

## Files

| File | What you'd learn there |
|---|---|
| [Progress.md](./Progress.md) | What setup work is done and what still blocks implementation |
| [checklist.md](./checklist.md) | Fields and decisions to fill before source and Terraform scaffolding |
