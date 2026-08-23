# Argo CD GitOps Bootstrap Plan

This plan records the owner-run Argo CD bootstrap flow. Codex can update this plan and inspect non-sensitive evidence, but the owner runs all Kubernetes and repository access commands.

## Inputs

| Field | Value |
|---|---|
| AWS account ID | Private, not committed |
| AWS region | `us-east-1` |
| EKS cluster name | Private, not committed |
| Kubernetes context | Owner-managed |
| Argo CD namespace | `argocd` |
| Install method | Helm |
| GitOps repository URL | `<implementation-repository-url>` |
| GitOps branch | `main` |
| Repository access method | Public read |
| Application name | `prediction-api-prod` |
| Application source path | `k8s/apps/prediction-api/chart` |
| Helm values file | `values-prod.yaml` |
| Destination namespace | `prediction-api` |

## Owner-Run Sequence

1. Confirm the Kubernetes context points at the demo EKS cluster.
2. Create the `argocd` namespace if it does not exist.
3. Install Argo CD with Helm using the implementation repository install notes at `k8s/platform/argocd/install-notes.md`.
4. Confirm `<implementation-repository-url>` is publicly readable by Argo CD.
5. Create the `prediction-api-prod` Application in the `argocd` namespace.
6. Confirm Argo CD renders `k8s/apps/prediction-api/chart` from `main` with `values-prod.yaml`.
7. Sync the Application after the manual approval and GitOps update path allows the production desired state.
8. Record sync, health, and rendered resource evidence in the evidence project.

[owner-commands.md](./owner-commands.md) turns this sequence into exact PowerShell commands for the owner to run.

## Application Shape

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: prediction-api-prod
  namespace: argocd
spec:
  project: default
  source:
    repoURL: <implementation-repository-url>
    targetRevision: main
    path: k8s/apps/prediction-api/chart
    helm:
      valueFiles:
        - values-prod.yaml
  destination:
    server: https://kubernetes.default.svc
    namespace: prediction-api
```

Add an automated sync policy only after the owner confirms that CD updates GitOps state solely after manual approval. Manual sync is acceptable for the first bootstrap proof.
