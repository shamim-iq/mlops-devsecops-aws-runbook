# Owner-Run Argo CD Bootstrap Commands

Run these commands from the implementation repository after reviewing the Terraform outputs and confirming the current Kubernetes context is the demo EKS cluster. Do not commit generated files, kubeconfig, private keys, tokens, or command output that includes account-specific values.

## Variables

```powershell
$env:AWS_PROFILE = "<deployment-aws-profile>"
$env:AWS_REGION = "us-east-1"
$env:EKS_CLUSTER_NAME = "<private-eks-cluster-name>"
$env:GITOPS_REPO_URL = "<implementation-repository-url>"
$env:GITOPS_BRANCH = "main"
$env:ARGOCD_REPOSITORY_ACCESS_METHOD = "public-read"
$env:ARGOCD_NAMESPACE = "argocd"
$env:APP_NAME = "prediction-api-prod"
$env:APP_NAMESPACE = "prediction-api"
$env:APP_PATH = "k8s/apps/prediction-api/chart"
```

## Confirm Cluster Context

```powershell
aws eks update-kubeconfig `
  --region $env:AWS_REGION `
  --name $env:EKS_CLUSTER_NAME `
  --profile $env:AWS_PROFILE

kubectl config current-context
kubectl get nodes
```

Stop if the context or nodes are not the demo EKS cluster.

## Install Argo CD With Helm

If `helm` is not on `PATH`, set a session alias to the local Visual Studio Kubernetes Tools install:

```powershell
Set-Alias helm "<local-helm-binary-path>"
helm version
```

```powershell
helm repo add argo https://argoproj.github.io/argo-helm
helm repo update argo

helm upgrade --install argocd argo/argo-cd `
  --namespace $env:ARGOCD_NAMESPACE `
  --create-namespace `
  --wait

kubectl get pods -n $env:ARGOCD_NAMESPACE
kubectl get crd applications.argoproj.io
```

## Configure Repository Access

The selected method is public read. No repository credential secret is required. Continue to the Application creation step.

If the repository becomes private later, use one private access option only.

### Private Fallback: Deploy Key

```powershell
$env:GITOPS_SSH_REPO_URL = "<git-ssh-repository-url>"
$env:GITOPS_DEPLOY_KEY_PATH = "<local-private-deploy-key-path>"

kubectl create secret generic gitops-repo-prediction-api `
  -n $env:ARGOCD_NAMESPACE `
  --from-literal=type=git `
  --from-literal=url=$env:GITOPS_SSH_REPO_URL `
  --from-file=sshPrivateKey=$env:GITOPS_DEPLOY_KEY_PATH `
  --dry-run=client -o yaml |
  kubectl label -f - argocd.argoproj.io/secret-type=repository --local -o yaml |
  kubectl apply -f -

$env:GITOPS_REPO_URL = $env:GITOPS_SSH_REPO_URL
```

### Private Fallback: GitHub App

```powershell
$env:GITHUB_APP_ID = "<github-app-id>"
$env:GITHUB_APP_INSTALLATION_ID = "<github-app-installation-id>"
$env:GITHUB_APP_PRIVATE_KEY_PATH = "<local-github-app-private-key-path>"

kubectl create secret generic gitops-repo-prediction-api `
  -n $env:ARGOCD_NAMESPACE `
  --from-literal=type=git `
  --from-literal=url=$env:GITOPS_REPO_URL `
  --from-literal=githubAppID=$env:GITHUB_APP_ID `
  --from-literal=githubAppInstallationID=$env:GITHUB_APP_INSTALLATION_ID `
  --from-file=githubAppPrivateKey=$env:GITHUB_APP_PRIVATE_KEY_PATH `
  --dry-run=client -o yaml |
  kubectl label -f - argocd.argoproj.io/secret-type=repository --local -o yaml |
  kubectl apply -f -
```

## Create The Application

```powershell
kubectl apply -n $env:ARGOCD_NAMESPACE -f <local-implementation-repo>\k8s\platform\argocd\prediction-api-prod-application.yaml
```

## Verify Repository, Render, And Sync State

```powershell
kubectl get application $env:APP_NAME -n $env:ARGOCD_NAMESPACE
kubectl describe application $env:APP_NAME -n $env:ARGOCD_NAMESPACE
kubectl get events -n $env:ARGOCD_NAMESPACE --sort-by=.lastTimestamp
```

Before syncing, confirm the Argo Rollouts resource types used by the chart exist:

```powershell
kubectl get crd rollouts.argoproj.io
kubectl get crd analysistemplates.argoproj.io
```

If the first bootstrap is allowed to sync manually, run:

```powershell
<local-argocd-cli-path> version --client
kubectl config set-context --current --namespace=$env:ARGOCD_NAMESPACE
argocd app get $env:APP_NAME --core
argocd app diff $env:APP_NAME --core
argocd app sync $env:APP_NAME --core
argocd app wait $env:APP_NAME --core --sync --health --timeout 300
argocd app get $env:APP_NAME --core
```

## Evidence To Capture

```powershell
kubectl get application $env:APP_NAME -n $env:ARGOCD_NAMESPACE -o wide
kubectl get rollout -n $env:APP_NAMESPACE
kubectl get svc -n $env:APP_NAMESPACE
kubectl get analysisrun -n $env:APP_NAMESPACE
```

Record only non-sensitive status, health, sync result, and resource names in the evidence project.
