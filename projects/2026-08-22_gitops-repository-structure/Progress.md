# GitOps Repository Structure Progress

## Current State

`active` - 2026-08-22. The implementation repository exists and the application branch is merged to `main`. The prediction API GitOps tree now has valid Kustomize resources for the namespace, service, Argo Rollouts rollout, Prometheus analysis template, production overlay, and image tag patch. `kubectl kustomize k8s/apps/prediction-api/overlays/prod` passes locally.

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
- [x] Replace prediction API base placeholders with Kubernetes manifests.
- [x] Add Argo Rollouts canary behavior.
- [x] Add Prometheus analysis template.
- [x] Add production Kustomize overlay.
- [x] Add CD-owned image tag patch file.
- [x] Fill platform install notes for Argo CD, Argo Rollouts, Prometheus, and EFK.
- [x] Validate production overlay with `kubectl kustomize`.

## Remaining

- [ ] Review and commit the GitOps structure changes.
- [ ] Push the `gitops-repository-structure` branch.
- [ ] Open the implementation pull request.
- [ ] Re-check platform add-on resource requests after Terraform defines EKS node capacity.
