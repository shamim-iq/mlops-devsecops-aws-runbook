# CI Access And Approval Pipeline Progress

## Current State

`active` - 2026-08-22. The CI and access project is scaffolded. No CI workflow, OIDC role, ECR push, or approval gate has been configured.

## Done

- [x] Record requirement for OIDC-assumed IAM roles.
- [x] Record that long-lived AWS access keys must not be used.
- [x] Record required CI steps: checkout, tests, linting, SAST, SCA, secrets scan, Terraform checks, Docker build, Trivy scan, and ECR push.
- [x] Record manual approval gate requirement before production deployment.
- [x] Record Codex boundary: no AWS mutation, no deployment profile use, no image push.

## Remaining

- [ ] Confirm CI/CD platform.
- [ ] Record ECR repository name.
- [ ] Record EKS cluster name.
- [ ] Record pipeline OIDC provider.
- [ ] Record pipeline IAM role name.
- [ ] Record local owner-run AWS access commands.
- [ ] Choose SAST tool.
- [ ] Choose SCA tool.
- [ ] Choose secrets scanner.
- [ ] Define scan failure thresholds.
- [ ] Define Terraform check commands.
- [ ] Define Docker image tag format.
- [ ] Define Trivy failure thresholds.
- [ ] Define ECR push command.
- [ ] Define manual approval gate.
- [ ] Record expected CI evidence.
