# Application Topology View

This project defines a developer-facing Kubernetes topology view for one application at a time. It starts from a namespace and app selector, then discovers live relationships across workload, network, storage, and configuration resources so developers can see how the application is actually wired.

## Owner

Project owner - Kubernetes cluster and repositories kept private.

## Status

`complete` - 2026-08-23. The implementation repository contains the first `kubectl`-based topology tool, tests, CI lint inclusion, read-only RBAC manifest, and generated live topology report at `topology/reports/prediction-api.md`. The owner verified read-only Kubernetes access for the `prediction-api` namespace, generated the report from live cluster state, scanned it for sensitive values, and merged the report into implementation `main`.

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

The first build lives in the implementation repository branch `application-topology-view-tool`. Python is the smallest fit because the current application already uses Python and a Markdown generator does not need a service runtime. Discovery shells out to `kubectl get ... -o json` instead of using the Kubernetes Python client so the tool avoids an extra HTTP dependency chain and stays close to the owner-run verification commands.

```text
topology/
  -> apps.yaml
  -> __init__.py
  -> topology_view/
     |-- cli.py
     |-- config.py
     |-- discover.py
     |-- graph.py
     `-- render_markdown.py
  -> reports/
     `-- prediction-api.md
```

Discovery runs with read-only Kubernetes credentials. The first generated report captures the live `prediction-api` Rollout, ReplicaSets, Pod, Service, ConfigMap, selector, and recent rollout events without exposing account identifiers or secrets.

## Next

1. Use `topology/reports/prediction-api.md` as demo evidence if the topology view helps explain the live deployment.
2. Regenerate the report after any meaningful Kubernetes topology change.
3. Keep the report out of public evidence if future output includes sensitive object names, account identifiers, local paths, or secret values.

## Files

| File | What you'd learn there |
|---|---|
| [Progress.md](./Progress.md) | What topology work is done and what remains |
| [checklist.md](./checklist.md) | Discovery scope, config fields, output, and RBAC decisions |
| [plan.md](./plan.md) | Ordered implementation steps for the first topology report |
| [owner-commands.md](./owner-commands.md) | Owner-run implementation, RBAC, verification, and report-generation commands |
