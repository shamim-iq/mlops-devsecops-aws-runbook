# Terraform AWS Infrastructure

This project defines the Terraform work package for the demo-owned AWS infrastructure. It covers Terraform layout, providers, variables, outputs, backend configuration, environment values, networking, ECR, EKS, CPU-only node capacity, IAM, OIDC trust, Secrets Manager entries, and least-privilege policies.

## Owner

Project owner - AWS account kept private, preferred region `us-east-1`.

## Status

`active` - 2026-08-22. Terraform scope is recorded. Terraform files, backend, variables, plans, and AWS resources have not been created.

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
|-- environments/
|   `-- demo.tfvars
`-- modules/
    |-- networking/
    |-- ecr/
    |-- eks/
    |-- iam/
    `-- secrets/
```

Terraform must tag demo-owned resources with `Project=minimal-mlops-devsecops-pipeline` so cleanup can distinguish demo resources from shared account resources.

> [CONFIRM] Terraform backend type, state bucket, lock table, final VPC design, node shape, and CI/CD OIDC provider are not finalized yet.

## Next

1. Choose local state or remote S3 plus DynamoDB state locking.
2. Create Terraform layout with providers, variables, outputs, backend configuration, and `environments/demo.tfvars`.
3. Define networking for the one-day demo.
4. Define ECR repository and image policy.
5. Define EKS cluster and CPU-only node capacity.
6. Define IAM roles, OIDC trust, Secrets Manager entries, and least-privilege policies.
7. Run `terraform fmt`.
8. Run `terraform validate`.
9. Owner runs `terraform plan` and reviews billable or permission-sensitive resources.
10. Owner runs `terraform apply` only after accepting the reviewed plan.

## Files

| File | What you'd learn there |
|---|---|
| [Progress.md](./Progress.md) | Terraform infrastructure work completed and remaining |
| [checklist.md](./checklist.md) | Terraform backend, modules, resources, and review gates |
