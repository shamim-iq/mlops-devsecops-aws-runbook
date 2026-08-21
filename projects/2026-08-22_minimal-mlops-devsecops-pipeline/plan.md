# Minimal MLOps DevSecOps Pipeline Plan

Verified 2026-08-22 from the supplied requirements.

This plan keeps CI and CD separate because the project is meant to demonstrate the delivery lifecycle clearly during an interview. The plan also keeps cleanup as a first-class phase, because the infrastructure is temporary and cost-limited.

## Gates

| Gate | Must be true before moving on |
|---|---|
| Requirements gate | Owner email, AWS account, region, CI/CD platform, and repository layout are recorded. |
| Cost gate | The selected EKS node shape and add-ons fit the INR 500 objective as closely as practical. |
| Security gate | SAST, SCA, secrets scan, DAST, and Trivy thresholds are explicit. |
| Approval gate | CD does not update GitOps manifests until manual approval is granted. |
| Rollout gate | Argo Rollouts promotes only when Prometheus analysis succeeds. |
| Cleanup gate | AWS console or CLI check shows no unwanted billable resources remain. |

## Build Order

1. Create a lightweight scikit-learn model and store the trained artifact as `model.pkl`.
2. Serve predictions through FastAPI with health and metrics endpoints.
3. Add unit tests and linting for the application.
4. Containerize the service with Docker.
5. Create Amazon ECR and configure image push access through OIDC-assumed IAM roles.
6. Build CI: checkout, validate, unit tests, SAST, SCA, secrets scan, Docker build, Trivy image scan, ECR push, approval gate.
7. Create the GitOps repository with application manifests, Argo Rollouts resources, and monitoring/logging install notes.
8. Provision the minimal CPU-only EKS cluster and worker node.
9. Install Argo CD and connect it to the GitOps repository.
10. Install Argo Rollouts and convert the application deployment to a canary rollout.
11. Install Prometheus and expose request count, success/failure rate, and latency metrics from the app.
12. Configure Argo Rollouts analysis against Prometheus metrics.
13. Install minimal EFK with Helm: Elasticsearch, Fluent Bit, and Kibana.
14. Build CD: after approval, update the GitOps image tag and let Argo CD reconcile.
15. Demonstrate a healthy release that promotes.
16. Demonstrate a bad release that fails analysis and rolls back.
17. Run cleanup and verify billing/resource state.

## Open Questions

| Question | Why it matters |
|---|---|
| What owner email should appear in the runbook? | Ownership rows should identify a real maintainer. |
| Which AWS region and account will host the demo? | Cost, EKS instance types, and IAM setup depend on region/account. |
| Which CI/CD platform will run CI and CD? | OIDC provider setup and approval gate syntax depend on the platform. |
| Are source and GitOps separate repositories? | The CD update path and Argo CD source of truth depend on this. |
| Which SAST, SCA, secrets scan, and DAST tools will be used? | Pipeline commands and failure thresholds depend on tool choice. |
| Which Prometheus thresholds define rollback? | Argo Rollouts needs concrete success conditions. |
| How much EFK retention is acceptable? | Logging can exceed the cost objective if retention is too large. |

## Cleanup Checklist

- [ ] Delete EKS application workloads.
- [ ] Delete Argo Rollouts resources.
- [ ] Delete Argo CD resources.
- [ ] Delete Prometheus resources.
- [ ] Delete EFK resources.
- [ ] Delete the EKS cluster.
- [ ] Confirm EC2 worker nodes are terminated.
- [ ] Delete ECR repository images that are not needed.
- [ ] Delete S3 objects and bucket if created.
- [ ] Delete unused Secrets Manager secrets.
- [ ] Remove temporary IAM roles, policies, and OIDC resources if they are demo-only.
- [ ] Remove unnecessary security groups and networking resources.
- [ ] Verify no unused AWS resources remain.
- [ ] Check the AWS billing and cost dashboard.
