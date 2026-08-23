# Application Topology View Plan

This plan builds the first read-only topology report for the `prediction-api` application. The output is a Markdown file with a Mermaid graph and compact tables so it can be reviewed in GitHub and reused as demo evidence.

## Owner

Project owner - Kubernetes cluster and repositories kept private.

## Status

`active` - 2026-08-23. The plan is ready for implementation in the implementation repository. No Kubernetes access, generated report, or code exists yet.

## Implementation Steps

1. Create `topology/apps.yaml` with `name`, `namespace`, and `selector` for `prediction-api`.
2. Add Python dependencies for Kubernetes API access and YAML parsing.
3. Create `topology/topology_view/config.py` to load and validate the app config.
4. Create `topology/topology_view/discover.py` to read Rollouts, Deployments, ReplicaSets, Pods, Services, Ingresses, ConfigMaps, Secrets, PersistentVolumeClaims, HorizontalPodAutoscalers, and Events.
5. Match workloads and Pods with selectors, owner references, and labels.
6. Match Services to Pods through Service selectors.
7. Match Ingresses to Services through backend references.
8. Match Pods to ConfigMaps, Secrets, PVCs, and ServiceAccounts through environment, volume, and image pull references.
9. Match HPAs to scale targets.
10. Attach recent Events to involved objects.
11. Create `topology/topology_view/graph.py` to emit Mermaid `flowchart LR`.
12. Create `topology/topology_view/render_markdown.py` to render the graph and detail tables.
13. Create `topology/topology_view/cli.py` with arguments for config path, app name, and output path.
14. Add a namespace-scoped read-only Role and RoleBinding manifest for the owner to apply.
15. Owner generates `topology/reports/prediction-api.md` after the demo cluster exists.
16. Owner reviews the report for sensitive values before it becomes demo evidence.

## Completion Criteria

The project is complete when the generated `prediction-api` topology report shows the active workload, service path, configuration references, storage references if present, autoscaling target if present, recent events, and rollout ownership without exposing secrets or account identifiers.
