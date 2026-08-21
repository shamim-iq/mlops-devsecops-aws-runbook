# GitOps Repository Structure Progress

## Current State

`active` - 2026-08-22. The GitOps repository exists and the initial structure is defined. No GitOps manifests have been pushed yet.

## Done

- [x] Record that GitOps must hold Kubernetes desired state.
- [x] Record required areas: application manifests, Argo Rollouts resources, Prometheus analysis templates, and Helm install notes.
- [x] Record that CD updates GitOps only after manual approval.
- [x] Record GitOps repository URL: `https://github.com/shamim-iq/mlops-devsecops-aws-gitops.git`.
- [x] Record GitOps default branch: `main`.
- [x] Decide separate repository versus folder in source repository: separate repository.
- [x] Decide environment layout: `prod` only for the demo.
- [x] Record Argo CD application source path: `apps/prediction-api/overlays/prod`.
- [x] Define the initial GitOps repository structure.
- [x] Document the first push steps for the owner.

## Remaining

- [ ] Push the initial GitOps repository structure.
- [ ] Fill application manifests.
- [ ] Fill Argo Rollouts canary behavior.
- [ ] Fill Prometheus analysis template thresholds.
- [ ] Fill Helm install notes and resource requests for platform add-ons.
