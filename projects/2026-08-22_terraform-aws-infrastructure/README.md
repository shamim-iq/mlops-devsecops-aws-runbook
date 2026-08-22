# Terraform AWS Infrastructure

This project defines the Terraform work package for the demo-owned AWS infrastructure. It covers Terraform layout, providers, variables, outputs, backend configuration, environment values, networking, ECR, EKS, CPU-only node capacity, IAM, OIDC trust, Secrets Manager entries, and least-privilege policies.

## Owner

Project owner - AWS account kept private, preferred region `us-east-1`.

## Status

`active` - 2026-08-22. Terraform resources are defined, applied by the owner, and verified with the read-only AWS profile. `terraform fmt -recursive`, `terraform validate`, and `terraform plan -var-file="envs/prod/demo.tfvars"` pass, with the final plan reporting no changes. Implementation repository changes are ready for owner review, staging, commit, and push.

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

Local state is the current demo choice. Remote S3 backend and DynamoDB locking are not configured because this is a one-owner, short-lived demo. Committed environment values live in `demo.tfvars.example`; the ignored local `demo.tfvars` file carries the deployment AWS CLI profile and concrete local values.

The applied stack includes a tagged demo VPC, two public subnets, two private subnets, an internet gateway, one NAT gateway, ECR repository with immutable tags and scan-on-push, EKS cluster, one CPU-only managed node group, EKS core add-ons, GitHub Actions OIDC roles, an EKS workload OIDC provider, and an empty Secrets Manager runtime secret container.

## Next

1. Owner reviews changed implementation files, then stages, commits, and pushes them.
2. Owner updates the pull request with the applied Terraform evidence.
3. Keep `terraform/envs/prod/demo.tfvars`, Terraform state, plan files, and local policy files with concrete account identifiers out of commits.
4. Run `terraform plan -var-file="envs/prod/demo.tfvars"` before later changes and expect no drift unless the owner intentionally changes the stack.
5. Clean up all demo AWS resources when the demonstration is finished.

## Files

| File | What you'd learn there |
|---|---|
| [Progress.md](./Progress.md) | Terraform infrastructure work completed and remaining |
| [checklist.md](./checklist.md) | Terraform backend, modules, resources, and review gates |
