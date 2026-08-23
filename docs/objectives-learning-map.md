# Objectives Learning Map

| Seq | Main objective / learnable point | Implemented by project |
|---:|---|---|
| 1 | Define scope, AWS region, cost boundaries, repository model, Terraform state choice, and owner/Codex operating boundaries. | `2026-08-22_mlops-devsecops-execution-setup` |
| 2 | Understand the full delivery lifecycle and gates: CI, CD, GitOps, rollout validation, logging, evidence, and cleanup. | `docs/plan.md` |
| 3 | Build the ML application baseline: scikit-learn model artifact, FastAPI health, prediction, metrics, tests, linting, dependency audit, and Docker build. | `2026-08-22_model-api-container-build` |
| 4 | Define Kubernetes desired state with Helm, namespace, service, Argo Rollouts `Rollout`, Prometheus `AnalysisTemplate`, and production values. | `2026-08-22_gitops-repository-structure` |
| 5 | Define demo AWS infrastructure with Terraform: networking, ECR, EKS, node capacity, add-ons, IAM/OIDC, and Secrets Manager. | `2026-08-22_terraform-aws-infrastructure` |
| 6 | Learn secure CI/CD access with OIDC-assumed roles, no long-lived AWS keys, CI checks, security scans, image scan, ECR push, and manual approval. | `2026-08-22_ci-access-and-approval-pipeline` |
| 7 | Bootstrap GitOps deployment with Argo CD, repository connection, application sync, and health verification. | `2026-08-22_argocd-gitops-bootstrap` |
| 8 | Add progressive delivery with Argo Rollouts, Prometheus metrics, canary analysis, promotion gates, and rollback/block behavior. | `2026-08-22_rollouts-prometheus-analysis` |
| 9 | Add minimal observability with Elasticsearch, Fluent Bit, Kibana, short retention, and searchable application logs. | `2026-08-22_minimal-efk-logging` |
| 10 | Prove CD behavior with approved GitOps image updates, Argo CD reconciliation, healthy promotion, forced failure, rollback, and restore. | `2026-08-22_cd-rollout-promotion-rollback` |
| 11 | Generate a live Kubernetes application topology report from workload, service, ConfigMap, ReplicaSet, Pod, and event relationships. | `2026-08-22_application-topology-view` |
| 12 | Capture final demo evidence for CI, scans, ECR, approval, GitOps update, Argo CD sync, workload health, rollout, rollback, and logs. | `2026-08-22_evidence-and-cleanup` |
| 13 | Plan cleanup after explicit owner approval: destroy review, Kubernetes teardown, Terraform destroy, AWS inventory check, and billing verification. | `2026-08-22_evidence-and-cleanup` |

## Key Learnable Points

1. How to scope a one-day, low-cost AWS MLOps demo without pretending it is production.
2. How to serve a simple ML model through FastAPI with health, prediction, and metrics endpoints.
3. How to containerize an ML API and prepare it for ECR/EKS.
4. How to separate CI from CD so quality/security checks and deployment approval are visible.
5. How OIDC replaces long-lived AWS keys in CI/CD.
6. How Terraform defines repeatable AWS infrastructure and why cleanup tags/state boundaries matter.
7. How GitOps makes Kubernetes desired state auditable through repo commits.
8. How Argo CD reconciles a Helm chart into EKS.
9. How Argo Rollouts performs canary delivery.
10. How Prometheus metrics can promote or block a rollout.
11. How to prove rollback behavior with evidence, not just claims.
12. How lightweight EFK gives searchable app/Kubernetes logs for demo proof.
13. How topology reports help explain live Kubernetes relationships.
14. How to package evidence for CV/interview storytelling.
15. How to safely plan cleanup without deleting anything before explicit approval.
