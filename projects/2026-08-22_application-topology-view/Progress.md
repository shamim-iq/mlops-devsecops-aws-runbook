# Application Topology View Progress

## Current State

`complete` - 2026-08-23. The topology requirement is implemented in the implementation repository and the generated live report is merged at `topology/reports/prediction-api.md`. The owner verified Kubernetes read access for `prediction-api`, generated the report from live cluster state, scanned it for sensitive values, and merged the evidence report.

## Done

- [x] Record requirement for an application-centric Kubernetes topology view.
- [x] Choose simple app config as the control surface.
- [x] Choose read-only Kubernetes discovery as the data source.
- [x] Define the first relationship set: workload, ReplicaSet, Pod, Service, Ingress, ConfigMap, Secret, PVC, ServiceAccount, HPA, and Events.
- [x] Decide not to use custom resource definitions for the first version.
- [x] Choose Markdown with Mermaid as the first output format.
- [x] Pick Python as the implementation language.
- [x] Record the first implementation file layout.
- [x] Record read-only RBAC requirements.
- [x] Record owner commands for implementation setup, RBAC review, verification, report generation, and public-safety scan.
- [x] Create implementation branch `application-topology-view-tool`.
- [x] Add topology config, CLI, config loader, discovery, graph, and Markdown renderer in the implementation repository.
- [x] Add read-only topology viewer RBAC manifest in the implementation repository.
- [x] Add topology unit tests and fixtures in the implementation repository.
- [x] Include `topology` in implementation CI linting.
- [x] Run implementation tests: 8 passed on 2026-08-23.
- [x] Run implementation linting: passed on 2026-08-23.
- [x] Run implementation dependency audit: no known vulnerabilities found on 2026-08-23.
- [x] Merge implementation branch `application-topology-view-tool`.
- [x] Verify read-only Kubernetes access for Pods and Secrets in namespace `prediction-api`.
- [x] Verify live Rollout, ReplicaSets, Pod, Service, ConfigMap, and Events are readable.
- [x] Fix `kubectl` JSON Pod parsing bug and add regression test.
- [x] Run implementation tests after fix: 9 passed on 2026-08-23.
- [x] Generate `topology/reports/prediction-api.md` from live cluster state.
- [x] Scan generated report for sensitive values: no matches on 2026-08-23.
- [x] Merge generated topology report into implementation `main`.

## Remaining

- [ ] Regenerate the report after meaningful topology changes.
- [ ] Use the generated report as demo evidence if it improves the final evidence package.
