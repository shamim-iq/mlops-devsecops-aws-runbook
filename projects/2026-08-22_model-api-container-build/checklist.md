# Model API Container Build Checklist

## Model

| Field | Value |
|---|---|
| Dataset | Built-in scikit-learn Iris dataset |
| Model type | Logistic Regression |
| Artifact path | `app/model/model.pkl` |
| Training script path | `scripts/train_model.py` candidate |
| CPU-only compatible | Yes |

## API

| Endpoint | Purpose | Status |
|---|---|---|
| `GET /health` | Health check for runtime and rollout probes | Created |
| `POST /predict` | Prediction request and response | Created with `model.pkl` loading |
| `GET /metrics` | Prometheus scrape endpoint | Created |

## Quality

| Check | Tool | Status |
|---|---|---|
| Unit tests | pytest | Passing: 3 tests on 2026-08-22 |
| Linting | | Not created |
| Dependency check | | Not created |
| Local API run command | uvicorn | Recorded in implementation README |
| Local test command | pytest | Recorded in implementation README |

## Container

| Item | Value |
|---|---|
| Dockerfile path | `Dockerfile` |
| Image name | `mlops-prediction-api` candidate |
| Local port | `8000` |
| Build command | `docker build -t mlops-prediction-api:local .` |
| Run command | `docker run --rm -p 8000:8000 mlops-prediction-api:local` |
| Health verification command | `curl http://localhost:8000/health` |
| Prediction verification command | `curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" -d "{\"feature_a\":1,\"feature_b\":1,\"feature_c\":0}"` |
| Metrics verification command | `curl http://localhost:8000/metrics` |

Do not move to ECR push or deployment work until the local container runs and the health, prediction, and metrics endpoints are verified.
