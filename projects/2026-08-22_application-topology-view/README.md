# Application Topology View

This project defines a developer-facing Kubernetes topology view for one application at a time. It starts from a namespace and app selector, then discovers live relationships across workload, network, storage, and configuration resources so developers can see how the application is actually wired.

## Owner

Project owner - Kubernetes cluster and repositories kept private.

## Status

`active` - 2026-08-23. Scope is defined, Python is selected for the first implementation, and Markdown with Mermaid is selected as the first output format. The first implementation plan is recorded. No implementation files, Kubernetes permissions, generated topology report, or CLI have been created.

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

## Implementation Plan

The first build should live in the implementation repository, not this runbook repository. Python is the smallest fit because the current application already uses Python, the Kubernetes client is mature, and a Markdown generator does not need a service runtime.

```text
topology/
  -> apps.yaml
  -> topology_view/
     |-- cli.py
     |-- config.py
     |-- discover.py
     |-- graph.py
     `-- render_markdown.py
  -> reports/
     `-- prediction-api.md
```

Discovery should run with read-only Kubernetes credentials. The first report can be generated manually by the owner after the demo cluster exists, then stored as evidence if it explains the deployment better than the Argo CD resource tree alone.

## Next

1. Add the topology tool files to the implementation repository.
2. Define the read-only Kubernetes Role and RoleBinding for the selected namespace.
3. Create `topology/apps.yaml` with the `prediction-api` namespace and selector.
4. Implement config loading and validation.
5. Implement Kubernetes discovery for workloads, ReplicaSets, Pods, Services, Ingresses, ConfigMaps, Secrets, PVCs, HPAs, and Events.
6. Implement Mermaid graph generation.
7. Implement Markdown detail tables.
8. Generate `topology/reports/prediction-api.md`.
9. Add the generated report to demo evidence if it is useful.

## Files

| File | What you'd learn there |
|---|---|
| [Progress.md](./Progress.md) | What topology work is done and what remains |
| [checklist.md](./checklist.md) | Discovery scope, config fields, output, and RBAC decisions |
| [plan.md](./plan.md) | Ordered implementation steps for the first topology report |
| [owner-commands.md](./owner-commands.md) | Owner-run implementation, RBAC, verification, and report-generation commands |
