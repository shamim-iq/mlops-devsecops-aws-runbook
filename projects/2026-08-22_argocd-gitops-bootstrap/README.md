# Argo CD GitOps Bootstrap

This project defines the Argo CD bootstrap work for the demo EKS cluster. It covers installing Argo CD in EKS, connecting Argo CD to the GitOps repository, and recording the application source path that Argo CD will reconcile.

## Owner

shamim.linkedin@gmail.com - AWS account `447182646004`, preferred region `us-east-1`.

## Status

`active` - 2026-08-22. The Argo CD bootstrap scope is recorded. EKS cluster name, GitOps repository URL, Argo CD install method, namespace, and application source path are not yet recorded.

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

> [CONFIRM] EKS cluster name, GitOps repository URL, Argo CD namespace, install method, repository access method, and Argo CD application path are not recorded yet.

## Next

1. Record the EKS cluster name after Terraform creates it.
2. Record the GitOps repository URL and branch.
3. Choose Argo CD install method: manifest, Helm, or Terraform-managed Helm release.
4. Record the Argo CD namespace.
5. Decide how Argo CD authenticates to the GitOps repository.
6. Define the Argo CD Application source path.
7. Owner installs Argo CD in EKS.
8. Owner connects Argo CD to the GitOps repository.
9. Owner verifies Argo CD can sync the desired state.

## Files

| File | What you'd learn there |
|---|---|
| [Progress.md](./Progress.md) | Argo CD bootstrap work completed and remaining |
| [checklist.md](./checklist.md) | Cluster, repository, install, and sync decisions |
