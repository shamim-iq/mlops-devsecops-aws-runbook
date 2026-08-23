# Argo CD GitOps Bootstrap Checklist

## Cluster

| Field | Value |
|---|---|
| AWS account ID | Private, not committed |
| AWS region | `us-east-1` |
| EKS cluster name | Private, not committed |
| Kubernetes context | Owner-managed |
| Argo CD namespace | `argocd` |

## GitOps Connection

| Field | Value |
|---|---|
| GitOps repository URL | `<implementation-repository-url>` |
| GitOps branch | `main` |
| Repository access method | Public read |
| Argo CD Application name | `prediction-api-prod` |
| Argo CD Application source path | `k8s/apps/prediction-api/chart` |
| Helm values file | `values-prod.yaml` |
| Argo CD Application destination namespace | `prediction-api` |

## Bootstrap Steps

| Step | Owner | Status |
|---|---|---|
| Install Argo CD | Owner | Done |
| Configure repository access | Owner | Not needed for public read |
| Create Argo CD Application | Owner | Done |
| Render Helm chart through Argo CD | Owner | Done |
| Verify repository connection | Owner | Done |
| Install local Argo CD CLI | Codex | Done |
| Verify Argo Rollouts CRDs | Owner | Done |
| Verify sync status | Owner | Done |
| Verify health status | Owner | Done |

Codex must not run Kubernetes commands against the cluster or create Argo CD resources.
