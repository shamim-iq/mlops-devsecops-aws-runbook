# GitOps Repository Structure

This project defines the Kubernetes desired-state layout inside the implementation repository before CD is implemented. It covers application manifests, Argo Rollouts resources, Prometheus analysis templates, and Helm install notes for Argo CD, Argo Rollouts, Prometheus, and minimal EFK.

## Owner

Project owner - AWS account kept private, preferred region `us-east-1`.

## Status

`active` - 2026-08-22. The implementation repository is `<implementation-repository-url>`, and the local working directory is `<local-implementation-repo>`. The repository holds the app, Terraform, CI, docs, and Kubernetes desired state together. The initial tracked structure was pushed to `main` at commit `18518cf`.

## Repository Shape

```text
MLOps-Project/
|-- README.md
|-- app/
|   |-- model/
|   `-- main.py
|-- tests/
|-- Dockerfile
|-- requirements.txt
|-- terraform/
|   |-- envs/
|   |   `-- prod/
|   `-- modules/
|-- k8s/
|   |-- apps/
|   |   `-- prediction-api/
|   |       |-- base/
|   |       |   |-- namespace.yaml
|   |       |   |-- service.yaml
|   |       |   |-- rollout.yaml
|   |       |   |-- analysis-template.yaml
|   |       |   `-- kustomization.yaml
|   |       `-- overlays/
|   |           `-- prod/
|   |               |-- kustomization.yaml
|   |               `-- image-tag.yaml
|   `-- platform/
|       |-- argocd/
|       |   `-- install-notes.md
|       |-- argo-rollouts/
|       |   `-- install-notes.md
|       |-- prometheus/
|       |   `-- install-notes.md
|       `-- efk/
|           `-- install-notes.md
|-- .github/
|   `-- workflows/
`-- docs/
    `-- install-notes.md
```

The same repository is both the implementation repo and the Kubernetes source of truth for Argo CD. The default branch is `main`. Argo CD should point at `k8s/apps/prediction-api/overlays/prod` for the production application source path. CI builds and pushes images, but CD changes the image tag under `k8s/` only after manual approval.

Keep rollout and analysis resources inside the Kubernetes application base so the Argo CD application applies one Kustomize tree. `terraform/` owns AWS infrastructure. `app/`, `tests/`, and the root Docker files own the FastAPI service. `k8s/platform/` holds install notes and values choices for Argo CD, Argo Rollouts, Prometheus, and EFK until those add-ons are installed. Add real Helm values files only when the chart and resource requests are selected.

## Next

1. Replace placeholder files with the FastAPI service skeleton and project README content.
2. Define the base Kubernetes manifests for the FastAPI prediction API.
3. Define Argo Rollouts canary behavior in `k8s/apps/prediction-api/base/rollout.yaml`.
4. Define Prometheus analysis in `k8s/apps/prediction-api/base/analysis-template.yaml`.
5. Record Helm install notes and resource requests for Argo CD, Argo Rollouts, Prometheus, and minimal EFK.

## Files

| File | What you'd learn there |
|---|---|
| [Progress.md](./Progress.md) | What GitOps structure decisions are done and what remains |
| [checklist.md](./checklist.md) | Repository layout and manifest decisions to confirm |
