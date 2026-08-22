# Terraform AWS Infrastructure Progress

## Current State

`active` - 2026-08-22. Terraform resources are implemented, applied by the owner, and verified with the read-only AWS profile. The deployed stack is in sync with Terraform: `terraform plan -var-file="envs/prod/demo.tfvars"` reports no changes. Implementation repository changes are not staged, committed, or pushed yet.

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
- [x] Define networking resources.
- [x] Define ECR resources.
- [x] Define EKS resources with CPU-only worker capacity.
- [x] Define IAM and OIDC resources.
- [x] Define Secrets Manager resources.
- [x] Configure Terraform to read the local AWS CLI profile from ignored `demo.tfvars`.
- [x] Owner ran `terraform plan`.
- [x] Owner reviewed billable resources.
- [x] Owner reviewed permission-sensitive resources.
- [x] Owner ran `terraform apply` after plan acceptance.
- [x] Verify deployment with read-only AWS profile.
- [x] Confirm final Terraform plan reports no changes.

## Remaining

- [ ] Owner reviews changed implementation files.
- [ ] Owner stages, commits, and pushes implementation repository changes.
- [ ] Owner updates the pull request with applied Terraform evidence.
- [ ] Keep local-only files and concrete AWS account identifiers out of committed runbook files.
- [ ] Clean up demo AWS resources when the demonstration is finished.
