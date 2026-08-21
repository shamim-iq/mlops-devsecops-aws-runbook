# Argo CD GitOps Bootstrap Checklist

## Cluster

| Field | Value |
|---|---|
| AWS account ID | Private, not committed |
| AWS region | `us-east-1` |
| EKS cluster name | |
| Kubernetes context | Owner-managed |
| Argo CD namespace | |

## GitOps Connection

| Field | Value |
|---|---|
| GitOps repository URL | |
| GitOps branch | |
| Repository access method | |
| Argo CD Application name | |
| Argo CD Application source path | |
| Argo CD Application destination namespace | |

## Bootstrap Steps

| Step | Owner | Status |
|---|---|---|
| Install Argo CD | Owner | Not done |
| Configure repository access | Owner | Not done |
| Create Argo CD Application | Owner | Not done |
| Verify repository connection | Owner | Not done |
| Verify sync status | Owner | Not done |

Codex must not run Kubernetes commands against the cluster or create Argo CD resources.
