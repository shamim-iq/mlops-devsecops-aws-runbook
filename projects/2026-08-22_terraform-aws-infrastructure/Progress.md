# Terraform AWS Infrastructure Progress

## Current State

`active` - 2026-08-22. Terraform infrastructure work package is scaffolded. No Terraform files or AWS resources have been created.

## Done

- [x] Record Terraform layout requirement.
- [x] Record required AWS resource groups: networking, ECR, EKS, IAM, OIDC, Secrets Manager, and least-privilege policies.
- [x] Record CPU-only node requirement.
- [x] Record `terraform fmt` and `terraform validate` gates.
- [x] Record owner-only `terraform plan` review and `terraform apply` boundary.

## Remaining

- [ ] Decide Terraform backend type.
- [ ] Record state bucket name if remote state is used.
- [ ] Record lock table name if remote state is used.
- [ ] Create `terraform/backend.tf`.
- [ ] Create `terraform/providers.tf`.
- [ ] Create `terraform/variables.tf`.
- [ ] Create `terraform/outputs.tf`.
- [ ] Create `terraform/environments/demo.tfvars`.
- [ ] Define networking module.
- [ ] Define ECR module.
- [ ] Define EKS module.
- [ ] Define IAM and OIDC module.
- [ ] Define Secrets Manager module.
- [ ] Run `terraform fmt`.
- [ ] Run `terraform validate`.
- [ ] Owner runs `terraform plan`.
- [ ] Owner reviews billable resources.
- [ ] Owner reviews permission-sensitive resources.
- [ ] Owner runs `terraform apply` after plan acceptance.
