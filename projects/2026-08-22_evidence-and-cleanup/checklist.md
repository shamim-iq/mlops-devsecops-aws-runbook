# Evidence And Cleanup Checklist

## Evidence

| Evidence | Source | Status |
|---|---|---|
| CI result | CI/CD platform | Not captured |
| SAST result | CI/CD platform or scanner output | Not captured |
| SCA result | CI/CD platform or scanner output | Not captured |
| Secrets scan result | CI/CD platform or scanner output | Not captured |
| Trivy image scan result | CI/CD platform or scanner output | Not captured |
| Image in ECR | AWS ECR console or CLI output | Not captured |
| Production approval | GitHub Actions environment approval | Not captured |
| GitOps image update | Repository commit or workflow output | Not captured |
| Argo CD sync | Argo CD UI or CLI output | Not captured |
| EKS workload health | Argo CD workload view or kubectl output | Not captured |
| Rollout promotion | Argo Rollouts UI or CLI output | Not captured |
| Prometheus analysis | Prometheus UI or AnalysisRun output | Not captured |
| Rollback | Argo Rollouts UI or CLI output | Not captured |
| Logs | Kibana or log query output | Not captured |
| Cleanup | Terraform and AWS verification output | Not captured |

## Destroy Review

| Check | Owner | Status |
|---|---|---|
| Run `terraform plan -destroy` | Owner | Not done |
| Review EKS deletion | Owner | Not done |
| Review ECR deletion | Owner | Not done |
| Review IAM deletion | Owner | Not done |
| Review Secrets Manager deletion | Owner | Not done |
| Review S3/DynamoDB state handling | Owner | Not done |
| Review networking deletion | Owner | Not done |

## Kubernetes Cleanup

| Resource group | Status |
|---|---|
| Application workloads | Not removed |
| Argo Rollouts resources | Not removed |
| Argo CD resources | Not removed |
| Prometheus resources | Not removed |
| EFK resources | Not removed |
| Helm releases | Not removed |
| Persistent volumes | Not checked |

## AWS Verification

| Area | Status |
|---|---|
| EKS cluster deleted | Not verified |
| EC2 worker nodes terminated | Not verified |
| ECR images deleted if not needed | Not verified |
| IAM demo roles and policies removed | Not verified |
| Secrets Manager demo secrets removed | Not verified |
| Security groups removed | Not verified |
| VPC/networking removed | Not verified |
| S3 artifacts or state buckets handled | Not verified |
| DynamoDB lock table handled | Not verified |
| Billing dashboard checked | Not verified |

Codex must not run destructive cleanup commands or use the `<deployment-aws-profile>` profile.
