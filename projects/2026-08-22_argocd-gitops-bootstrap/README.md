# Argo CD GitOps Bootstrap

This project defines the Argo CD bootstrap work for the demo EKS cluster. It covers installing Argo CD in EKS, connecting Argo CD to the GitOps repository, and recording the application source path that Argo CD will reconcile.

## Owner

Project owner - AWS account kept private, preferred region `us-east-1`.

## Status

`complete` - 2026-08-23. Argo CD is installed in the `argocd` namespace and reconciles the production `prediction-api` application from the implementation repository `main` branch at `k8s/apps/prediction-api/chart` with `values-prod.yaml`. Repository access is public read, so no Argo CD repository credential secret is needed. The owner verified the Argo Rollouts CRDs exist, synced `prediction-api-prod` to revision `3e8c83f`, and confirmed the Application is `Synced` and `Healthy`.

## Operating Boundary

Codex must not install Argo CD, access the EKS cluster with deployment credentials, create Kubernetes resources, or connect live repositories. The owner performs cluster and Argo CD changes with approved deployment access.

## Bootstrap Shape

```text
EKS cluster
  -> argocd namespace
  -> Argo CD install
  -> GitOps repository credentials or access configuration
  -> Argo CD Application
  -> sync desired state from GitOps repository
```

Argo CD must read from the GitOps repository as the source of truth. It should not deploy application changes outside the manual approval and GitOps update flow.

The bootstrap uses Helm because the implementation repository already records platform Helm install notes and Helm is used for the Kubernetes desired-state package. The Argo CD Application should target the in-cluster Kubernetes API and deploy the prediction API chart into the `prediction-api` namespace.

> [CONFIRM] The concrete EKS cluster name is not recorded in public docs.

## Next

1. Record non-sensitive Argo CD sync evidence in the evidence and cleanup project.
2. Continue with rollout, Prometheus analysis, and CD promotion or rollback proof.

## Files

| File | What you'd learn there |
|---|---|
| [Progress.md](./Progress.md) | Argo CD bootstrap work completed and remaining |
| [checklist.md](./checklist.md) | Cluster, repository, install, and sync decisions |
| [plan.md](./plan.md) | Owner-run bootstrap sequence and Argo CD Application shape |
| [owner-commands.md](./owner-commands.md) | Exact owner-run PowerShell commands for bootstrap |
