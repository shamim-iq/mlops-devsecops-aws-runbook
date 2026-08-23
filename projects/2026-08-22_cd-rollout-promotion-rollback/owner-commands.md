# CD Rollout Promotion Rollback Owner Commands

These commands are for the project owner to run after CI has pushed a healthy image tag and a deliberately bad image tag. They mirror the approved CD workflow for manual proof or replay, and they prove that GitOps updates, Argo CD reconciles the chart, Argo Rollouts promotes a healthy release, and Prometheus analysis rolls back a bad release.

## Boundary

Codex must not run these commands. The owner runs them with approved deployment access because they update GitOps, trigger deployment, read cluster state, and may affect live AWS resources.

## Inputs

| Input | Value |
|---|---|
| GitOps repository | `<implementation-repository-url>` |
| GitOps branch | `main` |
| Values file | `k8s/apps/prediction-api/chart/values-prod.yaml` |
| Argo CD application | `prediction-api-prod` |
| Namespace | `<prediction-api-namespace>` |
| Rollout | `<prediction-api-rollout-name>` |
| Healthy tag | `<healthy-image-tag>` |
| Bad tag | `<bad-image-tag>` |

## Local Variables

```powershell
$GitOpsRepo = "<local-implementation-repo>"
$ValuesFile = "k8s/apps/prediction-api/chart/values-prod.yaml"
$ArgoApp = "prediction-api-prod"
$Namespace = "<prediction-api-namespace>"
$Rollout = "<prediction-api-rollout-name>"
$HealthyTag = "<healthy-image-tag>"
$BadTag = "<bad-image-tag>"
```

## Healthy Release

Run this after the GitHub Actions production environment approval is granted.

```powershell
Set-Location $GitOpsRepo
git status --short
git switch main
git pull --ff-only
```

Update `image.tag` in `k8s/apps/prediction-api/chart/values-prod.yaml` to the healthy tag. Use `yq` if installed, otherwise edit the value manually.

```powershell
$env:RELEASE_TAG = $HealthyTag
yq -i '.image.tag = strenv(RELEASE_TAG)' $ValuesFile
git diff -- $ValuesFile
```

The owner stages, commits, and pushes the approved GitOps image tag change.

```powershell
git add $ValuesFile
git commit -m "chore: deploy prediction-api healthy image"
git push
```

Verify Argo CD and Argo Rollouts state. If automated sync is disabled, sync the application manually.

```powershell
argocd app get $ArgoApp
argocd app sync $ArgoApp
kubectl argo rollouts get rollout $Rollout -n $Namespace --watch
kubectl argo rollouts status $Rollout -n $Namespace
```

Capture evidence for the approval, values diff, Argo CD sync, rollout promotion, and Prometheus healthy analysis.

## Bad Release

Run this only after the healthy release is promoted and stable.

```powershell
Set-Location $GitOpsRepo
git status --short
git switch main
git pull --ff-only
```

Update `image.tag` to the bad tag.

```powershell
$env:RELEASE_TAG = $BadTag
yq -i '.image.tag = strenv(RELEASE_TAG)' $ValuesFile
git diff -- $ValuesFile
```

The owner stages, commits, and pushes the approved GitOps image tag change.

```powershell
git add $ValuesFile
git commit -m "chore: deploy prediction-api bad image"
git push
```

Watch the rollout fail analysis and return to the previous stable version.

```powershell
argocd app get $ArgoApp
argocd app sync $ArgoApp
kubectl argo rollouts get rollout $Rollout -n $Namespace --watch
kubectl argo rollouts status $Rollout -n $Namespace
```

Capture evidence for the bad release GitOps diff, Argo CD sync, failed Prometheus analysis, rollout abort, and rollback to the previous stable image.

## Evidence Names

| Evidence | Suggested file name |
|---|---|
| GitHub Actions approval | `cd-approval-healthy.png` |
| Healthy GitOps image tag change | `gitops-healthy-tag-diff.txt` |
| Healthy Argo CD sync | `argocd-healthy-sync.txt` |
| Healthy rollout promotion | `rollout-healthy-promoted.txt` |
| Bad GitOps image tag change | `gitops-bad-tag-diff.txt` |
| Bad Argo CD sync | `argocd-bad-sync.txt` |
| Failed Prometheus analysis | `prometheus-analysis-failed.txt` |
| Rollback result | `rollout-rollback.txt` |
