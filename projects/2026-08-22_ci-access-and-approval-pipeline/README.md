# CI Access And Approval Pipeline

This project defines local and pipeline access for ECR and EKS, then builds the CI flow up to image push and manual production approval. It covers OIDC-assumed IAM roles, application checks, security scans, Terraform checks, Docker build, Trivy image scan, ECR push, and the manual approval gate before production deployment.

## Owner

Project owner - AWS account kept private, preferred region `us-east-1`.

## Status

`active` - 2026-08-22. The CI and access scope is recorded. CI/CD platform, role names, ECR repository name, EKS cluster name, security tools, and approval mechanism are not yet finalized.

## Operating Boundary

Codex must not configure AWS resources, assume deployment roles, push images to ECR, update GitHub settings, or create pull requests. The owner configures OIDC roles and runs any pipeline or AWS actions that mutate resources.

## Pipeline Shape

```text
checkout
  -> install dependencies
  -> unit tests
  -> linting
  -> SAST
  -> SCA
  -> secrets scan
  -> terraform fmt
  -> terraform validate
  -> terraform plan check
  -> docker build
  -> Trivy image scan
  -> ECR push
  -> manual approval gate
```

Pipeline authentication uses OIDC-assumed IAM roles instead of long-lived AWS access keys. Production deployment must not continue until the manual approval gate passes.

> [CONFIRM] CI/CD platform, OIDC role names, ECR repository name, EKS cluster name, SAST tool, SCA tool, secrets scanner, Terraform plan mode, and approval mechanism are not recorded yet.

## Next

1. Confirm CI/CD platform.
2. Record ECR repository and EKS cluster names after Terraform creates them.
3. Define local AWS access commands for owner-run checks.
4. Define pipeline OIDC role assumption.
5. Select SAST, SCA, secrets scanning, and Trivy thresholds.
6. Create CI workflow steps for tests, linting, scans, Terraform checks, Docker build, image scan, and ECR push.
7. Add the manual approval gate before production deployment.
8. Record evidence expected from a successful CI run.

## Files

| File | What you'd learn there |
|---|---|
| [Progress.md](./Progress.md) | CI access and pipeline work completed and remaining |
| [checklist.md](./checklist.md) | Access, CI, security, image, and approval decisions |
