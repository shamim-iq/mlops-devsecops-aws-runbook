# Application Topology View Progress

## Current State

`active` - 2026-08-23. The application topology view exists. It maps source, CI, ECR, approval, GitOps, Argo CD, EKS, Argo Rollouts, Prometheus, EFK, evidence, and cleanup from the current runbook state. The evidence map and public-safe runtime identifier placeholders are recorded. Owner-provided evidence is still required before completion.

## Done

- [x] Create the project README.
- [x] Record the topology purpose.
- [x] Map source repository, CI, image registry, GitOps, runtime, rollout, metrics, logs, evidence, and cleanup.
- [x] Record that production deployment depends on manual approval before the GitOps image tag update.
- [x] Record that Argo CD reconciles the Helm chart source path.
- [x] Record that Argo Rollouts uses Prometheus analysis for promotion or rollback.
- [x] Create the topology checklist.
- [x] Link the topology project from the central plan file index.
- [x] Create the evidence map.
- [x] Record public-safe runtime identifier placeholders.
- [x] Align topology evidence categories with the evidence and cleanup checklist.

## Remaining

- [ ] Owner records evidence storage location.
- [ ] Add owner-provided ECR image evidence reference.
- [ ] Add owner-provided manual approval evidence reference.
- [ ] Add owner-provided GitOps image update evidence reference.
- [ ] Add owner-provided Argo CD sync evidence reference.
- [ ] Add owner-provided EKS workload health evidence reference.
- [ ] Add owner-provided rollout promotion evidence reference.
- [ ] Add owner-provided rollback evidence reference.
- [ ] Add owner-provided Prometheus analysis evidence reference.
- [ ] Add owner-provided application log evidence reference.
- [ ] Add owner-provided cleanup verification reference.
- [ ] Mark the topology view complete after evidence and cleanup boundaries are recorded.
