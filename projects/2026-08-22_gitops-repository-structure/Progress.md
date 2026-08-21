# GitOps Repository Structure Progress

## Current State

`active` - 2026-08-22. The implementation repository exists and the initial single-repository structure is pushed to `main` at commit `18518cf`. Kubernetes manifests are placeholders only.

## Done

- [x] Record that GitOps must hold Kubernetes desired state.
- [x] Record required areas: application manifests, Argo Rollouts resources, Prometheus analysis templates, and Helm install notes.
- [x] Record that CD updates GitOps only after manual approval.
- [x] Record implementation repository URL: `<implementation-repository-url>`.
- [x] Record GitOps default branch: `main`.
- [x] Decide repository model: single repository for app, Terraform, CI, docs, and Kubernetes desired state.
- [x] Decide environment layout: `prod` only for the demo.
- [x] Record Argo CD application source path: `k8s/apps/prediction-api/overlays/prod`.
- [x] Define the initial single-repository structure.
- [x] Create the local `k8s/` and Terraform subfolder structure in `<local-implementation-repo>`.
- [x] Document the first push steps for the owner.
- [x] Add placeholder files so Git tracks the structure.
- [x] Push the initial single-repository structure.

## Remaining

- [ ] Replace placeholder files with real app, Terraform, and Kubernetes content.
- [ ] Fill application manifests.
- [ ] Fill Argo Rollouts canary behavior.
- [ ] Fill Prometheus analysis template thresholds.
- [ ] Fill Helm install notes and resource requests for platform add-ons.
