# Model API Container Build Checklist

## Model

| Field | Value |
|---|---|
| Dataset | |
| Model type | |
| Artifact path | `app/model/model.pkl` |
| Training script path | |
| CPU-only compatible | Yes |

## API

| Endpoint | Purpose | Status |
|---|---|---|
| `GET /health` | Health check for runtime and rollout probes | Not created |
| `POST /predict` | Prediction request and response | Not created |
| `GET /metrics` | Prometheus scrape endpoint | Not created |

## Quality

| Check | Tool | Status |
|---|---|---|
| Unit tests | | Not created |
| Linting | | Not created |
| Dependency check | | Not created |
| Local API run command | | Not recorded |
| Local test command | | Not recorded |

## Container

| Item | Value |
|---|---|
| Dockerfile path | `Dockerfile` |
| Image name | |
| Local port | |
| Build command | |
| Run command | |
| Health verification command | |
| Prediction verification command | |
| Metrics verification command | |

Do not move to ECR push or deployment work until the local container runs and the health, prediction, and metrics endpoints are verified.
