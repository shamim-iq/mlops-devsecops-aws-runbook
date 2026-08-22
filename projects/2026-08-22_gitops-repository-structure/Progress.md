# GitOps Repository Structure Progress

## Current State

`active` - 2026-08-22. The implementation repository exists and the application branch is merged to `main`. The prediction API GitOps structure was changed from Kustomize to a Helm chart because the owner wants to avoid learning Kustomize for this demo. The chart has templates for the namespace, service, Argo Rollouts rollout, and Prometheus analysis template, plus default and production values. Helm 4.2.4 is installed locally, `helm lint` passes, and `helm template` renders the chart with `values-prod.yaml`.

## Done

- [x] Record that GitOps must hold Kubernetes desired state.
- [x] Record required areas: application manifests, Argo Rollouts resources, Prometheus analysis templates, and Helm install notes.
- [x] Record that CD updates GitOps only after manual approval.
- [x] Record implementation repository URL: `<implementation-repository-url>`.
- [x] Record GitOps default branch: `main`.
- [x] Decide repository model: single repository for app, Terraform, CI, docs, and Kubernetes desired state.
- [x] Decide environment layout: `prod` only for the demo.
- [x] Record Argo CD application source path: `k8s/apps/prediction-api/chart`.
- [x] Define the initial single-repository structure.
- [x] Create the local `k8s/` and Terraform subfolder structure in `<local-implementation-repo>`.
- [x] Document the first push steps for the owner.
- [x] Add placeholder files so Git tracks the structure.
- [x] Push the initial single-repository structure.
- [x] Replace Kustomize structure with a prediction API Helm chart.
- [x] Add Helm template for the namespace.
- [x] Add Helm template for the service.
- [x] Add Helm template for Argo Rollouts canary behavior.
- [x] Add Helm template for the Prometheus analysis template.
- [x] Add `values.yaml` for local defaults.
- [x] Add `values-prod.yaml` for CD-owned image repository and tag values.
- [x] Fill platform install notes for Argo CD, Argo Rollouts, Prometheus, and EFK.
- [x] Install Helm locally: 4.2.4.
- [x] Run `helm lint` for the prediction API chart.
- [x] Run `helm template` with `values-prod.yaml`.

## Remaining

- [ ] Commit and push the Helm chart conversion.
- [ ] Open or update the implementation pull request.
- [ ] Re-check platform add-on resource requests after Terraform defines EKS node capacity.
