# Argo CD GitOps Bootstrap Progress

## Current State

`complete` - 2026-08-23. Argo CD is installed in the demo EKS cluster in the `argocd` namespace, with all core pods running and the `applications.argoproj.io` custom resource definition present. The `prediction-api-prod` Application reconciles the implementation repository `main` branch at `k8s/apps/prediction-api/chart` with `values-prod.yaml`. After Argo Rollouts CRDs were installed, the owner synced the Application to revision `3e8c83f` and verified it is `Synced` and `Healthy`.

## Done

- [x] Record requirement to install Argo CD in EKS.
- [x] Record requirement to connect Argo CD to the GitOps repository.
- [x] Record that GitOps remains the source of truth.
- [x] Record owner-only boundary for EKS and Kubernetes changes.
- [x] Record GitOps repository URL placeholder.
- [x] Record GitOps branch: `main`.
- [x] Choose Argo CD install method: Helm.
- [x] Record Argo CD namespace: `argocd`.
- [x] Define Argo CD Application name: `prediction-api-prod`.
- [x] Define Argo CD Application source path: `k8s/apps/prediction-api/chart`.
- [x] Define Helm values file: `values-prod.yaml`.
- [x] Define destination namespace: `prediction-api`.
- [x] Draft owner-run Argo CD bootstrap command sequence.
- [x] Create local-only bootstrap environment note at `.env.argocd-gitops-bootstrap.local`.
- [x] Choose repository access method: public read.
- [x] Owner updated kubeconfig for the demo EKS cluster.
- [x] Owner verified the Kubernetes context and a ready EKS node.
- [x] Owner installed Argo CD with Helm in the `argocd` namespace.
- [x] Owner verified Argo CD pods are running.
- [x] Owner verified the `applications.argoproj.io` custom resource definition exists.
- [x] Create `prediction-api-prod` Argo CD Application manifest in the implementation repository.
- [x] Owner recreated the Argo CD Application from the implementation repository manifest.
- [x] Owner verified Argo CD can read the repository and render chart resources.
- [x] Install local Argo CD CLI `v3.5.1` at a private local path.
- [x] Owner verified local Argo CD CLI runs in PowerShell.
- [x] Owner verified Argo CD core mode can read `prediction-api-prod`.
- [x] Owner attempted manual sync and confirmed it fails on missing Argo Rollouts CRDs.
- [x] Owner verified `rollouts.argoproj.io` CRD exists.
- [x] Owner verified `analysistemplates.argoproj.io` CRD exists.
- [x] Owner synced `prediction-api-prod` to revision `3e8c83f`.
- [x] Owner verified `prediction-api-prod` is `Synced`.
- [x] Owner verified `prediction-api-prod` is `Healthy`.

## Remaining

- [ ] Record non-sensitive sync evidence in the evidence and cleanup project.
