# Application Topology View

This project defines a developer-facing Kubernetes topology view for one application at a time. It starts from a namespace and app selector, then discovers live relationships across workload, network, storage, and configuration resources so developers can see how the application is actually wired.

## Owner

Project owner - Kubernetes cluster and repositories kept private.

## Status

`active` - 2026-08-22. Scope is defined and Markdown with Mermaid is selected as the first output format. No implementation files, Kubernetes permissions, generated topology report, or CLI have been created.

## How It Works

Use one small config file per app. The tool should not require developers to describe every Kubernetes object by hand because the cluster already has the relationship data.

```yaml
apps:
  - name: prediction-api
    namespace: prediction-api
    selector:
      app.kubernetes.io/name: prediction-api
```

The topology builder reads Kubernetes with read-only permissions, then follows standard relationships:

```text
Rollout or Deployment -> ReplicaSet -> Pod
Service -> Pod selector
Ingress -> Service backend
Pod -> ConfigMap, Secret, PVC, ServiceAccount
PVC -> PersistentVolume
HPA -> scale target
Events -> involved object
```

The first output is a Markdown report with a Mermaid graph and short resource detail tables. Markdown with Mermaid is the smallest useful format because it works in GitHub pull requests, runbook evidence, and local previews without a hosted service.

Keep configuration intentionally small:

| Field | Purpose |
|---|---|
| `name` | Display name for the app |
| `namespace` | Namespace to query |
| `selector` | Labels that identify the app's pods and workload resources |

Do not introduce custom resource definitions for the topology tool. Standard Kubernetes labels, owner references, selectors, and references are enough for the first version.

## Next

1. Pick implementation language: Python is the smallest fit for this repo.
2. Define the read-only Kubernetes permissions.
3. Create the app config file format.
4. Build the discovery logic for workloads, services, ingress, config, secrets, storage, and events.
5. Generate `topology/prediction-api.md` with a Mermaid graph and resource detail tables.
6. Add the generated report to demo evidence if it is useful.

## Files

| File | What you'd learn there |
|---|---|
| [Progress.md](./Progress.md) | What topology work is done and what remains |
| [checklist.md](./checklist.md) | Discovery scope, config fields, output, and RBAC decisions |
