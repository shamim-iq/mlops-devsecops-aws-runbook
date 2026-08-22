# Terraform AWS Infrastructure Progress

## Current State

`active` - 2026-08-22. Terraform root files, local backend note, environment values, module directories, and module interfaces are created in `<local-implementation-repo>`. Terraform 1.15.8 is installed locally. `terraform fmt -recursive`, `terraform init -backend=false`, and `terraform validate` pass. No AWS resources have been planned, created, changed, or deleted.

## Done

- [x] Record Terraform layout requirement.
- [x] Record required AWS resource groups: networking, ECR, EKS, IAM, OIDC, Secrets Manager, and least-privilege policies.
- [x] Record CPU-only node requirement.
- [x] Record `terraform fmt` and `terraform validate` gates.
- [x] Record owner-only `terraform plan` review and `terraform apply` boundary.
- [x] Choose local state for the initial demo scaffold.
- [x] Create Terraform root files.
- [x] Create `terraform/envs/prod/demo.tfvars.example`.
- [x] Create module directories for networking, ECR, EKS, IAM, and secrets.
- [x] Create module variable and output interfaces.
- [x] Install Terraform locally: 1.15.8.
- [x] Run `terraform fmt -recursive`.
- [x] Run `terraform init -backend=false`.
- [x] Run `terraform validate`: passed.

## Remaining

- [ ] Define networking resources.
- [ ] Define ECR resources.
- [ ] Define EKS resources.
- [ ] Define IAM and OIDC resources.
- [ ] Define Secrets Manager resources.
- [ ] Re-run `terraform fmt`.
- [ ] Re-run `terraform validate`.
- [ ] Owner runs `terraform plan`.
- [ ] Owner reviews billable resources.
- [ ] Owner reviews permission-sensitive resources.
- [ ] Owner runs `terraform apply` after plan acceptance.
