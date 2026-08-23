# Application Topology View Checklist

## Components

| Component | Role | Status |
|---|---|---|
| Implementation repository | Source, app, Terraform, CI, GitOps desired state | Recorded |
| FastAPI prediction API | Serves health, prediction, and metrics endpoints | Recorded |
| Docker image | Deployable application package | Recorded |
| GitHub Actions CI | Tests, checks, scans, build, image push | Recorded |
| Amazon ECR | Stores approved container images | Evidence needed |
| Manual approval | Gates production GitOps update | Evidence needed |
| GitOps Helm chart | Kubernetes desired state for prediction API | Recorded |
| Argo CD | Reconciles desired state into EKS | Evidence needed |
| Amazon EKS | Runtime cluster for the demo workload | Evidence needed |
| Argo Rollouts | Canary promotion and rollback controller | Evidence needed |
| Prometheus | Metrics source for rollout analysis | Evidence needed |
| EFK | Short-retention log evidence | Evidence needed |
| Cleanup | Removes demo-owned billable resources | Evidence needed |

## Topology Links

| Link | Expected proof | Status |
|---|---|---|
| Source to CI | Successful workflow run | Needed |
| CI to ECR | Image tag present in ECR | Needed |
| Approval to GitOps update | Production approval record and image tag commit | Needed |
| GitOps to Argo CD | Argo CD application source path and sync state | Needed |
| Argo CD to EKS | Workload reconciled in the target namespace | Needed |
| Service to rollout | Rollout owns the active ReplicaSets | Needed |
| Metrics to analysis | Prometheus query result and AnalysisRun status | Needed |
| Failed release to rollback | Aborted rollout and stable ReplicaSet retained | Needed |
| Workload to logs | Application logs visible through EFK | Needed |
| Demo to cleanup | Destroy and inventory checks complete | Needed |

## Evidence Map

| Topology link | Evidence needed | Owner command or source | Evidence location | Status |
|---|---|---|---|---|
| Source to CI | Successful workflow run with tests and checks | GitHub Actions run page | `<evidence-location>` | Needed |
| Security checks | SAST, SCA, secrets scan, and Trivy results | GitHub Actions run page or scanner output | `<evidence-location>` | Needed |
| CI to ECR | Pushed image tag visible in ECR | AWS ECR console or owner-run AWS CLI output | `<evidence-location>` | Needed |
| Approval to GitOps update | Production approval record and image tag commit | GitHub Actions environment approval and repository history | `<evidence-location>` | Needed |
| GitOps to Argo CD | Argo CD application source path, revision, and sync state | Argo CD UI or owner-run Argo CD CLI output | `<evidence-location>` | Needed |
| Argo CD to EKS | Prediction API workload healthy in the target namespace | Owner-run `kubectl` output or Argo CD workload view | `<evidence-location>` | Needed |
| Service to rollout | Healthy release promoted by Argo Rollouts | Argo Rollouts UI or owner-run kubectl/rollouts output | `<evidence-location>` | Needed |
| Metrics to analysis | Prometheus query and AnalysisRun result | Prometheus UI, Argo Rollouts output, or owner-run kubectl output | `<evidence-location>` | Needed |
| Failed release to rollback | Failed analysis, aborted rollout, and stable ReplicaSet retained | Argo Rollouts UI or owner-run kubectl/rollouts output | `<evidence-location>` | Needed |
| Workload to logs | Application logs visible through Kibana or log query output | Kibana screenshot or owner-run log query output | `<evidence-location>` | Needed |
| Demo to cleanup | Destroy review, destroy completion, resource inventory, and billing check | Terraform output, AWS console, or owner-run AWS CLI output | `<evidence-location>` | Needed |

## Stable Identifiers

| Item | Value |
|---|---|
| AWS account ID | Private, not committed |
| Preferred AWS region | `us-east-1` |
| CI/CD platform | GitHub Actions |
| ECR repository | `<ecr-repository-name>` |
| EKS cluster | `<eks-cluster-name>` |
| Kubernetes namespace | `<application-namespace>` |
| Kubernetes service | `<prediction-api-service-name>` |
| GitOps branch | `main` |
| Argo CD application name | `prediction-api-prod` |
| Argo CD source path | `k8s/apps/prediction-api/chart` |
| Production values file | `k8s/apps/prediction-api/chart/values-prod.yaml` |
| Production image tag value | `image.tag` |

## Boundaries

| Boundary | Rule |
|---|---|
| AWS changes | Owner only |
| Kubernetes changes | Owner only |
| Git staging, commits, pushes, and pull requests | Owner only |
| Public docs | No personal details, account identifiers, local paths, or secrets |
| Cost | Keep the demo temporary and clean up all demo-owned resources |
