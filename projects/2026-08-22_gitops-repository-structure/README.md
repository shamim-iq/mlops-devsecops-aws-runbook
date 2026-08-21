# GitOps Repository Structure

This project defines the GitOps repository layout for Kubernetes desired state before CD is implemented. It covers application manifests, Argo Rollouts resources, Prometheus analysis templates, and Helm install notes for Argo CD, Argo Rollouts, Prometheus, and minimal EFK.

## Owner

shamim.linkedin@gmail.com - AWS account `447182646004`, preferred region `us-east-1`.

## Status

`active` - 2026-08-22. The GitOps structure requirement is recorded. The GitOps repository location, repository name, and manifest layout are not yet finalized.

## Repository Shape

```text
<gitops-repo>/
|-- apps/
|   `-- prediction-api/
|       |-- base/
|       `-- overlays/
|           `-- prod/
|-- rollouts/
|   `-- prediction-api/
|-- analysis/
|   `-- prometheus/
|-- platform/
|   |-- argocd/
|   |-- argo-rollouts/
|   |-- prometheus/
|   `-- efk/
`-- docs/
    `-- install-notes.md
```

The repository is the Kubernetes source of truth for Argo CD. CI builds and pushes images, but CD changes the image tag in this GitOps repository only after manual approval.

> [CONFIRM] GitOps repository URL, branch, environment layout, and final Helm chart choices are not recorded yet.

## Next

1. Decide whether GitOps uses a separate repository or a folder in the source repository.
2. Record the GitOps repository URL and default branch.
3. Choose the environment layout: `prod` only or `dev` plus `prod`.
4. Define the base Kubernetes manifests for the FastAPI prediction API.
5. Define Argo Rollouts canary resources.
6. Define Prometheus analysis templates for promotion and rollback.
7. Record Helm install notes for Argo CD, Argo Rollouts, Prometheus, and minimal EFK.

## Files

| File | What you'd learn there |
|---|---|
| [Progress.md](./Progress.md) | What GitOps structure decisions are done and what remains |
| [checklist.md](./checklist.md) | Repository layout and manifest decisions to confirm |
