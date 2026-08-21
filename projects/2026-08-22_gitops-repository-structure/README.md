# GitOps Repository Structure

This project defines the GitOps repository layout for Kubernetes desired state before CD is implemented. It covers application manifests, Argo Rollouts resources, Prometheus analysis templates, and Helm install notes for Argo CD, Argo Rollouts, Prometheus, and minimal EFK.

## Owner

shamim.linkedin@gmail.com - AWS account `447182646004`, preferred region `us-east-1`.

## Status

`active` - 2026-08-22. The GitOps repository exists at `https://github.com/shamim-iq/mlops-devsecops-aws-gitops.git`. The initial layout, default branch, Argo CD source path, and first push steps are defined. No GitOps manifests have been committed yet.

## Repository Shape

```text
mlops-devsecops-aws-gitops/
|-- README.md
|-- apps/
|   `-- prediction-api/
|       |-- base/
|       |   |-- namespace.yaml
|       |   |-- service.yaml
|       |   |-- rollout.yaml
|       |   |-- analysis-template.yaml
|       |   `-- kustomization.yaml
|       `-- overlays/
|           `-- prod/
|               |-- kustomization.yaml
|               `-- image-tag.yaml
|-- platform/
|   |-- argocd/
|   |   `-- install-notes.md
|   |-- argo-rollouts/
|   |   `-- install-notes.md
|   |-- prometheus/
|   |   `-- install-notes.md
|   `-- efk/
|       `-- install-notes.md
`-- docs/
    `-- install-notes.md
```

The repository is the Kubernetes source of truth for Argo CD. The default branch is `main`. Argo CD should point at `apps/prediction-api/overlays/prod` for the production application source path. CI builds and pushes images, but CD changes the image tag in this GitOps repository only after manual approval.

Keep rollout and analysis resources inside the application base so the Argo CD application applies one Kustomize tree. Platform folders hold install notes and values choices for Argo CD, Argo Rollouts, Prometheus, and EFK until those add-ons are installed. Add real Helm values files only when the chart and resource requests are selected.

## Next

1. Push the empty GitOps folder structure.
2. Define the base Kubernetes manifests for the FastAPI prediction API.
3. Define Argo Rollouts canary behavior in `apps/prediction-api/base/rollout.yaml`.
4. Define Prometheus analysis in `apps/prediction-api/base/analysis-template.yaml`.
5. Record Helm install notes and resource requests for Argo CD, Argo Rollouts, Prometheus, and minimal EFK.

## Files

| File | What you'd learn there |
|---|---|
| [Progress.md](./Progress.md) | What GitOps structure decisions are done and what remains |
| [checklist.md](./checklist.md) | Repository layout and manifest decisions to confirm |
