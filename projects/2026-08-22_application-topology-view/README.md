# Application Topology View

This project creates the single view of the demo application topology across source, CI, container registry, GitOps, EKS runtime, progressive delivery, metrics, logs, evidence, and cleanup. It exists so the owner can explain the deployed system without reconstructing it from separate project notes.

## Owner

Project owner - AWS account kept private, preferred region `us-east-1`, CI/CD platform GitHub Actions.

## Status

`active` - 2026-08-23. The topology project has started. The first topology map is based on the current runbook state: Terraform infrastructure is recorded as applied and verified, the application container path is recorded, the GitOps chart path is recorded, and the CD promotion and rollback proof is recorded. Live AWS, Kubernetes, Argo CD, Prometheus, EFK, and billing state still need owner-provided evidence before this view can be marked complete.

## Application Topology

```text
Developer workstation
  -> implementation repository
     |-- app and tests
     |-- Dockerfile
     |-- Terraform
     |-- GitHub Actions workflows
     `-- k8s/apps/prediction-api/chart
  -> GitHub Actions CI
     |-- tests, linting, dependency audit, security scans
     |-- Docker build
     `-- Trivy image scan
  -> Amazon ECR
  -> manual production approval
  -> GitOps image tag update
  -> Argo CD Application: prediction-api-prod
  -> EKS cluster
     |-- prediction API namespace
     |-- Argo Rollouts canary
     |-- Kubernetes Service
     |-- Prometheus scrape and rollout analysis
     `-- EFK log collection
  -> promotion, rollback, evidence, cleanup
```

The implementation repository is both the application source and the GitOps source of truth. CI may build, scan, and push an image, but production deployment waits for manual approval before the GitOps image tag changes. Argo CD reconciles the approved desired state into EKS, then Argo Rollouts controls the canary. Prometheus analysis decides promotion or rollback, and EFK provides short-retention log evidence.

## Runtime Boundary

The prediction API is a CPU-only FastAPI service that loads `app/model/model.pkl` and exposes health, prediction, and Prometheus metrics endpoints. Kubernetes desired state lives in the Helm chart at `k8s/apps/prediction-api/chart`, with production image values in `values-prod.yaml`.

The AWS footprint is demo-owned and temporary: tagged networking, ECR, EKS, one CPU-only managed node group, IAM/OIDC access, and Secrets Manager runtime secret container. Cleanup remains part of the topology because the demo is cost-controlled and short-lived.

## Runtime Identifier Placeholders

| Item | Value |
|---|---|
| AWS account ID | Private, not committed |
| AWS region | `us-east-1` |
| ECR repository | `<ecr-repository-name>` |
| EKS cluster | `<eks-cluster-name>` |
| Kubernetes namespace | `<application-namespace>` |
| Kubernetes service | `<prediction-api-service-name>` |
| Argo CD application | `prediction-api-prod` |
| GitOps branch | `main` |
| GitOps chart path | `k8s/apps/prediction-api/chart` |
| Production values file | `k8s/apps/prediction-api/chart/values-prod.yaml` |
| Production image tag value | `image.tag` |

## Evidence Targets

The topology is complete only when the owner can point to evidence for each link in the chain: CI result, image in ECR, manual approval, GitOps image update, Argo CD sync, healthy rollout promotion, failed rollout rollback, Prometheus analysis result, application logs, and cleanup verification.

> [CONFIRM] Live Argo CD, EKS, Prometheus, EFK, ECR, and cleanup evidence locations are not recorded in this project yet.

## Next

1. Owner records the evidence storage location.
2. Owner captures evidence for the CI result, ECR image, manual approval, GitOps image update, Argo CD sync, EKS workload health, rollout promotion, rollback, Prometheus analysis, logs, and cleanup verification.
3. Replace placeholder runtime identifiers with non-sensitive names after the owner confirms them.
4. Align this topology view with the final evidence and cleanup project before cleanup starts.
5. Mark this project complete after the evidence chain and cleanup boundary are recorded.

## Files

| File | What you'd learn there |
|---|---|
| [Progress.md](./Progress.md) | Topology view work completed and remaining |
| [checklist.md](./checklist.md) | Components, links, evidence, and cleanup boundaries to verify |
