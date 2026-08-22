# GitOps Repository Structure

This project defines the Kubernetes desired-state layout inside the implementation repository before CD is implemented. It covers the prediction API Helm chart, Argo Rollouts resources, Prometheus analysis template, and Helm install notes for Argo CD, Argo Rollouts, Prometheus, and minimal EFK.

## Owner

Project owner - AWS account kept private, preferred region `us-east-1`.

## Status

`active` - 2026-08-22. The implementation repository is `<implementation-repository-url>`, and the local working directory is `<local-implementation-repo>`. The repository holds the app, Terraform, CI, docs, and Kubernetes desired state together. The prediction API desired state is now a small Helm chart with namespace, service, Argo Rollouts `Rollout`, Prometheus `AnalysisTemplate`, default values, and production image values. Helm 4.2.4 is installed locally, `helm lint` passes, and `helm template` renders the chart with `values-prod.yaml`.

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
|   |       `-- chart/
|   |           |-- Chart.yaml
|   |           |-- values.yaml
|   |           |-- values-prod.yaml
|   |           `-- templates/
|   |               |-- namespace.yaml
|   |               |-- service.yaml
|   |               |-- rollout.yaml
|   |               |-- analysis-template.yaml
|   |               `-- _helpers.tpl
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

The same repository is both the implementation repo and the Kubernetes source of truth for Argo CD. The default branch is `main`. Argo CD should point at `k8s/apps/prediction-api/chart` for the production application source path and render it with `values-prod.yaml`. CI builds and pushes images, but CD changes the image repository and tag values only after manual approval.

Keep rollout and analysis resources inside the prediction API chart so Argo CD renders one application package. `terraform/` owns AWS infrastructure. `app/`, `tests/`, and the root Docker files own the FastAPI service. `k8s/platform/` holds install notes and values choices for Argo CD, Argo Rollouts, Prometheus, and EFK until those add-ons are installed.

## Next

1. Commit and push the Helm chart conversion.
2. Open or update the implementation pull request for review.
3. Start Terraform AWS infrastructure after the desired-state structure is merged.

## Files

| File | What you'd learn there |
|---|---|
| [Progress.md](./Progress.md) | What GitOps structure decisions are done and what remains |
| [checklist.md](./checklist.md) | Repository layout and manifest decisions to confirm |
