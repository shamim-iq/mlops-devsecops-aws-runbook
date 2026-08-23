# Application Topology View Progress

## Current State

`active` - 2026-08-23. The topology requirement is captured as a separate project, Python is selected for the first implementation, and Markdown with Mermaid is selected as the first output format. No code, RBAC, generated topology report, or CLI exists yet.

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

## Remaining

- [ ] Add topology tool files to the implementation repository.
- [ ] Define read-only RBAC.
- [ ] Create app config schema.
- [ ] Build Kubernetes discovery.
- [ ] Generate Mermaid graph output.
- [ ] Generate Markdown detail tables.
- [ ] Generate `topology/reports/prediction-api.md`.
- [ ] Add evidence to the portfolio/demo if the output is useful.
