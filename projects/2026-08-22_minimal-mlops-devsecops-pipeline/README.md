# Minimal End-to-End MLOps and DevSecOps Pipeline on AWS

This project builds a small scikit-learn model-serving system to demonstrate the operational lifecycle of an ML application. It packages a FastAPI prediction API into Docker, publishes the image to Amazon ECR, deploys it to CPU-only Amazon EKS through GitOps, validates rollout health with Prometheus, and rolls back automatically when validation fails. The work is for learning and CV demonstration, so the architecture favors clarity, low cost, and cleanup over production-grade availability.

## Owner

Iqbal <email not provided> - AWS account, region, and CI/CD platform not yet recorded.

## Status

`active` - 2026-08-22. Requirements captured and runbook scaffolded. No AWS resources, repositories, pipelines, or cluster workloads have been created yet.

## How it works

The application trains or packages a lightweight scikit-learn model as `model.pkl` and serves predictions through FastAPI. CI checks the application, runs SAST, SCA, secrets scanning, builds the Docker image, scans it with Trivy, and pushes the approved image to Amazon ECR. After manual approval, CD updates the image version in the GitOps repository. Argo CD reconciles the desired state into EKS, and Argo Rollouts sends a small canary slice to the new version. Prometheus metrics decide whether the rollout promotes or returns traffic to the previous version.

```text
Source repo
  -> CI: tests, SAST, SCA, secrets scan, Docker build, Trivy
  -> Amazon ECR
  -> manual approval
  -> GitOps repo image update
  -> Argo CD sync
  -> Argo Rollouts canary
  -> Prometheus analysis
  -> promote or rollback
```

The EKS footprint stays CPU-only and temporary. EFK provides searchable Kubernetes and application logs through Elasticsearch, Fluent Bit, and Kibana deployed by Helm, with minimal retention and data volume so logging does not dominate the cost target.

## Next

1. Confirm the owner email, AWS account, AWS region, CI/CD platform, and repository layout.
2. Choose the smallest EKS node shape and networking approach that can run EKS, Argo CD, Argo Rollouts, Prometheus, and minimal EFK inside the INR 500 cost objective.
3. Create the source and GitOps repository structure.
4. Build the FastAPI plus scikit-learn model service and local tests.
5. Define CI security thresholds for SAST, SCA, secrets scanning, DAST, and Trivy.
6. Implement OIDC-based AWS role assumption and Secrets Manager access.
7. Provision ECR and the temporary EKS cluster.
8. Install Argo CD, Argo Rollouts, Prometheus, and EFK with Helm.
9. Wire the canary rollout and Prometheus analysis.
10. Prove promotion and automatic rollback with one healthy and one failing deployment.
11. Run and record full cleanup, then verify AWS billing and leftover resources.

## Files

| File | What you'd learn there |
|---|---|
| [plan.md](./plan.md) | The one-day build order, gates, rollback proof, and cleanup sequence |
