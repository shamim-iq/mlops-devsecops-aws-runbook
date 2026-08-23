# Application Topology View Checklist

## Configuration

| Field | Value |
|---|---|
| Config style | One small YAML file |
| Required app fields | `name`, `namespace`, `selector` |
| First app | `prediction-api` |
| Custom resource definitions | No |

## Discovery

| Resource | Relationship source | Include first |
|---|---|---|
| Rollout | Argo Rollouts object selector and owner references | Yes |
| Deployment | Deployment selector and owner references | Yes |
| ReplicaSet | Owner references and labels | Yes |
| Pod | Owner references, labels, volumes, env, service account | Yes |
| Service | Label selector and ports | Yes |
| Ingress | Backend service references | Yes |
| ConfigMap | Pod env, envFrom, and volume references | Yes |
| Secret | Pod env, envFrom, imagePullSecrets, and volume references | Yes |
| PVC | Pod volume claim references | Yes |
| PersistentVolume | PVC binding | Later if storage is used |
| HPA | Scale target reference | Yes |
| Events | Involved object reference | Yes |

## Output

| Option | Status |
|---|---|
| Markdown with Mermaid graph | Selected |
| Static HTML report | Later if Markdown is not enough |
| Live dashboard | Later |
| Argo CD built-in resource tree only | Not enough for this requirement |

Generate one Markdown file per application. Each report should include one Mermaid graph followed by compact tables for workloads, pods, services, ingress, configuration, storage, and recent events.

## First Report

| Field | Value |
|---|---|
| Output path | `topology/prediction-api.md` |
| Graph format | Mermaid `flowchart LR` |
| Detail format | Markdown tables |
| Generated from | Read-only Kubernetes API discovery |
