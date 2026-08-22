# Terraform AWS Infrastructure

This project defines the Terraform work package for the demo-owned AWS infrastructure. It covers Terraform layout, providers, variables, outputs, backend configuration, environment values, networking, ECR, EKS, CPU-only node capacity, IAM, OIDC trust, Secrets Manager entries, and least-privilege policies.

## Owner

Project owner - AWS account kept private, preferred region `us-east-1`.

## Status

`active` - 2026-08-22. Terraform root files, local backend note, environment values, module directories, and module interfaces are created in `<local-implementation-repo>`. Terraform 1.15.8 is installed locally. `terraform fmt -recursive`, `terraform init -backend=false`, and `terraform validate` pass. No AWS resources have been planned, created, changed, or deleted.

## Operating Boundary

Codex must not deploy, change, provision, or delete AWS resources. Codex may help design Terraform files and run local formatting or validation that does not contact or mutate AWS. The owner runs `terraform plan` and `terraform apply` with the `<deployment-aws-profile>` AWS profile after reviewing billable and permission-sensitive resources.

## Terraform Shape

```text
terraform/
|-- backend.tf
|-- providers.tf
|-- variables.tf
|-- outputs.tf
|-- main.tf
|-- versions.tf
|-- envs/
|   `-- prod/
|       `-- demo.tfvars.example
`-- modules/
    |-- networking/
    |-- ecr/
    |-- eks/
    |-- iam/
    `-- secrets/
```

Terraform must tag demo-owned resources with `Project=minimal-mlops-devsecops-pipeline` so cleanup can distinguish demo resources from shared account resources.

Local state is the current demo choice. Remote S3 backend and DynamoDB locking are not configured because this is a one-owner, short-lived demo and no AWS resources should be created before plan review. Committed environment values live in `demo.tfvars.example`; the owner copies them to an ignored local `demo.tfvars` file before planning.

> [CONFIRM] Final VPC design, node shape, and CI/CD OIDC provider are not finalized yet.

## Next

1. Define networking resources after VPC/subnet review.
2. Define ECR repository and image policy.
3. Define EKS cluster and CPU-only node capacity.
4. Define IAM roles, OIDC trust, Secrets Manager entries, and least-privilege policies.
5. Re-run `terraform fmt`.
6. Re-run `terraform validate`.
7. Owner runs `terraform plan` and reviews billable or permission-sensitive resources.
8. Owner runs `terraform apply` only after accepting the reviewed plan.

## Files

| File | What you'd learn there |
|---|---|
| [Progress.md](./Progress.md) | Terraform infrastructure work completed and remaining |
| [checklist.md](./checklist.md) | Terraform backend, modules, resources, and review gates |
