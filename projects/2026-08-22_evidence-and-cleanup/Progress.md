# Evidence And Cleanup Progress

## Current State

`active` - 2026-08-22. The evidence and cleanup project is scaffolded. No evidence has been captured and no cleanup actions have been performed.

## Done

- [x] Record required evidence categories.
- [x] Record requirement to review `terraform plan -destroy`.
- [x] Record requirement to remove Kubernetes workloads and add-ons gracefully.
- [x] Record requirement to run `terraform destroy` for demo-owned AWS infrastructure.
- [x] Record requirement to verify AWS billing and resource inventory.
- [x] Record owner-only boundary for destructive and billable-resource actions.

## Remaining

- [ ] Record evidence storage location.
- [ ] Capture CI result.
- [ ] Capture security scan result.
- [ ] Capture ECR image evidence.
- [ ] Capture Argo CD sync evidence.
- [ ] Capture rollout promotion evidence.
- [ ] Capture rollback evidence.
- [ ] Capture logging evidence.
- [ ] Capture cleanup evidence.
- [ ] Owner runs `terraform plan -destroy`.
- [ ] Owner reviews resources marked for deletion.
- [ ] Owner removes Kubernetes workloads.
- [ ] Owner removes Kubernetes add-ons.
- [ ] Owner runs `terraform destroy`.
- [ ] Owner verifies AWS resource inventory.
- [ ] Owner verifies AWS billing and cost dashboard.
