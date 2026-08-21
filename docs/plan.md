# Minimal MLOps DevSecOps Pipeline Plan

Verified 2026-08-22 from the supplied requirements and execution setup decisions.

This project builds a small scikit-learn model-serving system to demonstrate the operational lifecycle of an ML application. It packages a FastAPI prediction API into Docker, publishes the image to Amazon ECR, deploys it to CPU-only Amazon EKS through GitOps, validates rollout health with Prometheus, and rolls back automatically when validation fails. The work is for learning and CV demonstration, so the architecture favors clarity, low cost, and cleanup over production-grade availability.

This plan keeps CI and CD separate because the project is meant to demonstrate the delivery lifecycle clearly during an interview. The implementation repository `<implementation-repository-url>` holds the app, Terraform, CI, docs, and Kubernetes desired state together. Terraform creates the AWS infrastructure so the demo can be repeated, reviewed, and destroyed from code. Cleanup remains a first-class phase because the infrastructure is temporary and cost-limited.

## Owner

Project owner - AWS account kept private, preferred region `us-east-1`, CI/CD platform GitHub Actions.

## Status

`active` - 2026-08-22. Requirements captured, execution setup decisions recorded, the implementation repository exists, the initial single-repository structure is pushed to `main` at commit `18518cf`, and the first FastAPI skeleton passes local tests. No AWS resources, pipelines, trained model artifact, valid Kubernetes manifests, or cluster workloads have been created.

## How It Works

The application trains or packages a lightweight scikit-learn model as `model.pkl` and serves predictions through FastAPI. CI checks the application, runs SAST, software composition analysis (SCA), secrets scanning, builds the Docker image, scans it with Trivy, and pushes the approved image to Amazon ECR. After manual approval, CD updates the image version in the GitOps repository. Argo CD reconciles the desired state into EKS, and Argo Rollouts sends a small canary slice to the new version. Prometheus metrics decide whether the rollout promotes or returns traffic to the previous version.

```text
Source repo
  -> CI: tests, SAST, SCA, secrets scan, Docker build, Trivy
  -> Amazon ECR
  -> manual approval
  -> k8s image tag update
  -> Argo CD sync
  -> Argo Rollouts canary
  -> Prometheus analysis
  -> promote or rollback
```

The EKS footprint stays CPU-only and temporary. The current candidate uses one `t3.medium` worker, avoids NAT Gateway, and keeps the cluster short-lived because the EKS control plane costs USD 0.10 per cluster-hour before worker nodes, storage, IPv4, data transfer, and logs. EFK provides searchable Kubernetes and application logs through Elasticsearch, Fluent Bit, and Kibana deployed by Helm, with an 8 GiB gp3 storage candidate and 1-day retention so logging does not dominate the cost target.

## Gates

| Gate | Must be true before moving on |
|---|---|
| Requirements gate | AWS account, region, CI/CD platform, and repository layout are recorded. |
| Cost gate | The selected EKS node shape, add-ons, NAT choice, and logging retention fit the INR 500 objective as closely as practical. |
| Terraform gate | Terraform backend, variables, providers, and module layout are recorded before any AWS resource is created. Local state is the current demo choice. |
| Security gate | SAST, SCA, secrets scan, DAST, and Trivy thresholds are explicit. |
| Approval gate | CD does not update GitOps manifests until manual approval is granted. |
| Rollout gate | Argo Rollouts promotes only when Prometheus analysis succeeds. |
| Cleanup gate | `terraform destroy` completes and AWS console or CLI checks show no unwanted billable resources remain. |

## Scope Sequence

1. Requirements and cost boundaries.
2. Repository layout and branching model.
3. Application model and FastAPI service.
4. Local tests, linting, and container build.
5. Terraform-managed AWS infrastructure.
6. IAM, OIDC, and Secrets Manager access.
7. CI pipeline with quality and security gates.
8. GitOps repository and Kubernetes desired state.
9. Argo CD installation and sync.
10. Argo Rollouts canary deployment.
11. Prometheus metrics and rollout analysis.
12. Minimal EFK logging.
13. CD pipeline with manual approval.
14. Healthy release demonstration.
15. Failed release and automatic rollback demonstration.
16. Evidence capture for CV and interview review.
17. Terraform destroy and AWS cleanup verification.

## Execution Steps

1. Record the AWS account, AWS region, CI/CD platform, source repository, GitOps repository, and Terraform state location. Done in execution setup.
2. Confirm the EKS node shape, add-ons, and logging retention fit the INR 500 cost-control objective as closely as practical. Done for the initial candidate; re-check after Helm resource requests are defined.
3. Create the single implementation repository structure for the FastAPI service, Docker build, tests, CI workflow, Terraform, Kubernetes desired state, and project docs. Initial folders exist in `<local-implementation-repo>`.
4. Push the initial repository structure to `<implementation-repository-url>`. Done at commit `18518cf`.
5. Build the lightweight scikit-learn model and store the trained artifact as `model.pkl`.
6. Build the FastAPI prediction API with health and metrics endpoints. Initial baseline API exists locally.
7. Add unit tests, linting, dependency checks, and local run commands for the application. First tests pass locally and run commands exist; linting and dependency checks remain.
8. Containerize the API with Docker and verify the container runs locally.
9. Create the Terraform layout with providers, variables, outputs, backend configuration, and environment-specific values.
10. Define Terraform for demo-owned AWS infrastructure: networking, ECR, EKS, CPU-only node capacity, IAM roles, OIDC trust, Secrets Manager entries, and least-privilege policies.
11. Run `terraform fmt` and `terraform validate`.
12. Owner runs `terraform plan` and reviews every billable or permission-sensitive resource before apply.
13. Owner runs `terraform apply` after the plan is accepted.
14. Configure local and pipeline access to the created ECR repository and EKS cluster through OIDC-assumed IAM roles.
15. Build CI: checkout, application tests, linting, SAST, SCA, secrets scan, Terraform fmt/validate/plan check, Docker build, Trivy image scan, and ECR push.
16. Add the manual approval gate before production deployment.
17. Install Argo CD in EKS and connect it to the GitOps repository.
18. Install Argo Rollouts and convert the application deployment to a canary rollout.
19. Install Prometheus and expose request count, success/failure rate, and latency metrics from the app.
20. Configure Argo Rollouts analysis against Prometheus metrics.
21. Install minimal EFK with Helm: Elasticsearch, Fluent Bit, and Kibana.
22. Build CD so the approved deployment updates the GitOps image tag and lets Argo CD reconcile the cluster.
23. Run a healthy release and verify Argo Rollouts promotes it.
24. Run a bad release and verify Prometheus analysis fails it and Argo Rollouts rolls it back.
25. Capture evidence for the CV/demo: CI result, security scan result, image in ECR, Argo CD sync, rollout promotion, rollback, logs, and cleanup.
26. Run `terraform plan -destroy` and review the resources marked for deletion.
27. Remove Kubernetes workloads and add-ons that need graceful teardown before infrastructure deletion.
28. Run `terraform destroy` for demo-owned AWS infrastructure.
29. Verify AWS billing and resource inventory show no unwanted billable resources remain.

## Open Questions

| Question | Why it matters |
|---|---|
| Which Terraform resources are demo-owned versus pre-existing? | Cleanup must not destroy shared account resources. |
| Which SAST, SCA, secrets scan, and DAST tools will be used? | Pipeline commands and failure thresholds depend on tool choice. |
| Which Prometheus thresholds define rollback? | Argo Rollouts needs concrete success conditions. |
| Does one `t3.medium` still fit after Helm resource requests are set? | Add-on memory requests may force a larger node or reduced add-on footprint. |
| Does local Terraform state remain acceptable before Terraform starts? | It is simple for the demo, but remote state is safer if collaboration starts. |

## Cleanup Checklist

- [ ] Run `terraform plan -destroy` and review the resources marked for deletion.
- [ ] Delete EKS application workloads.
- [ ] Delete Argo Rollouts resources.
- [ ] Delete Argo CD resources.
- [ ] Delete Prometheus resources.
- [ ] Delete EFK resources.
- [ ] Run `terraform destroy` for demo-owned AWS infrastructure.
- [ ] Confirm the EKS cluster is deleted.
- [ ] Confirm EC2 worker nodes are terminated.
- [ ] Confirm ECR repository images that are not needed are deleted.
- [ ] Confirm S3 objects and bucket are deleted if created for Terraform state or artifacts.
- [ ] Confirm unused Secrets Manager secrets are deleted.
- [ ] Confirm temporary IAM roles, policies, and OIDC resources are removed if they are demo-only.
- [ ] Confirm unnecessary security groups and networking resources are removed.
- [ ] Verify no unused AWS resources remain.
- [ ] Check the AWS billing and cost dashboard.

## Files

| File | What you'd learn there |
|---|---|
| [Execution setup](../projects/2026-08-22_mlops-devsecops-execution-setup/README.md) | AWS facts, cost checks, and source repository structure before implementation |
| [GitOps repository structure](../projects/2026-08-22_gitops-repository-structure/README.md) | Kubernetes desired state, rollout resources, Prometheus analysis, and Helm install notes |
| [Model API container build](../projects/2026-08-22_model-api-container-build/README.md) | Model artifact, FastAPI service, tests, quality checks, and Docker verification |
| [Terraform AWS infrastructure](../projects/2026-08-22_terraform-aws-infrastructure/README.md) | Terraform layout, AWS resource definitions, validation, plan review, and owner-only apply |
| [CI access and approval pipeline](../projects/2026-08-22_ci-access-and-approval-pipeline/README.md) | OIDC access, CI checks, image scan and push, and manual approval gate |
| [Argo CD GitOps bootstrap](../projects/2026-08-22_argocd-gitops-bootstrap/README.md) | Argo CD installation, GitOps repository connection, and sync verification |
| [Rollouts Prometheus analysis](../projects/2026-08-22_rollouts-prometheus-analysis/README.md) | Argo Rollouts canary delivery, Prometheus metrics, and analysis templates |
| [Minimal EFK logging](../projects/2026-08-22_minimal-efk-logging/README.md) | Helm-based Elasticsearch, Fluent Bit, Kibana, retention, storage, and log verification |
| [CD rollout promotion rollback](../projects/2026-08-22_cd-rollout-promotion-rollback/README.md) | GitOps image updates, Argo CD reconciliation, healthy promotion, and failed rollback proof |
| [Evidence and cleanup](../projects/2026-08-22_evidence-and-cleanup/README.md) | CV/demo evidence, destroy review, workload teardown, Terraform destroy, billing and inventory verification |
