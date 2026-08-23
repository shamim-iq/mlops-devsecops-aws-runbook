# Application Topology View Progress

## Current State

`active` - 2026-08-23. The topology requirement is captured as a separate project, Python is selected for the first implementation, and Markdown with Mermaid is selected as the first output format. The implementation repository branch `application-topology-view-tool` contains the first `kubectl`-based topology tool, tests, CI lint inclusion, and read-only RBAC manifest. Live Kubernetes verification and report generation remain owner-run.

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

## Remaining

- [ ] Owner reviews implementation branch changes.
- [ ] Owner stages, commits, and pushes implementation branch `application-topology-view-tool`.
- [ ] Owner opens implementation repository pull request.
- [ ] Owner applies or verifies read-only RBAC.
- [ ] Generate `topology/reports/prediction-api.md`.
- [ ] Scan generated topology report for sensitive values.
- [ ] Add evidence to the portfolio/demo if the output is useful.
