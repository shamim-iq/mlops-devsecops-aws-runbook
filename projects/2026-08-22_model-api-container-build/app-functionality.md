# Prediction App Functionality

The prediction app is a small FastAPI service that demonstrates how an ML model becomes a deployable application artifact. It is intentionally simple: train a lightweight classifier, save it as `model.pkl`, load it when the API starts, and expose a prediction endpoint that can be tested, containerized, scanned, deployed, monitored, and rolled back.

## What It Predicts

The model uses the built-in scikit-learn Iris dataset. Each training row describes an iris flower with numeric measurements, and the label is the flower class.

The demo API uses three numeric input fields:

| API field | Meaning in the demo |
|---|---|
| `feature_a` | First numeric model feature |
| `feature_b` | Second numeric model feature |
| `feature_c` | Third numeric model feature |

The response returns:

| Field | Meaning |
|---|---|
| `prediction` | Predicted class id |
| `score` | Highest class probability from the model |
| `model_version` | Version string stored with the artifact |

This is not meant to be a business-grade flower classifier. It is a compact ML-serving workload for proving the MLOps path: train, package, test, containerize, deploy, observe, promote, and roll back.

## How Training Works

The training entry point is `scripts/train_model.py` in the implementation repository. It loads the Iris dataset from scikit-learn, selects the first three dataset features to match the API request shape, and trains a Logistic Regression classifier.

```text
load Iris dataset
  -> select first three numeric features
  -> scale features with StandardScaler
  -> train LogisticRegression
  -> package model, version, feature names, and target names
  -> write app/model/model.pkl
```

The trained artifact contains the preprocessing step and classifier together in a scikit-learn pipeline. That keeps inference simple because the API can pass raw numeric fields to the loaded pipeline and get class probabilities back.

The artifact version is:

```text
iris-logreg-0.1.0
```

## How The API Uses The Model

The API starts by loading `app/model/model.pkl`. The `/predict` endpoint accepts the three numeric fields, builds a one-row feature array, and calls the loaded model.

```text
POST /predict
  -> validate JSON request with Pydantic
  -> convert fields into model feature array
  -> call predict_proba
  -> call predict
  -> return class id, confidence score, and model version
```

The score is the highest probability across the model's possible classes. It is rounded for a stable API response.

## Runtime Endpoints

| Endpoint | Purpose |
|---|---|
| `GET /health` | Runtime health check for local tests, container checks, and Kubernetes probes |
| `POST /predict` | Model inference endpoint |
| `GET /metrics` | Prometheus metrics endpoint |

The metrics endpoint exposes request counters and prediction latency. Argo Rollouts and Prometheus can use these metrics later to decide whether a canary release should promote or roll back.

## Why This App Fits The Demo

The app is small enough to run on a CPU-only EKS node, quick enough to build during the demo, and complete enough to exercise the real lifecycle:

```text
model artifact
  -> FastAPI app
  -> pytest
  -> ruff
  -> pip-audit
  -> Docker image
  -> Helm chart
  -> Argo CD
  -> Argo Rollouts
  -> Prometheus validation
```

The value of the app is not model accuracy. The value is that it behaves like a real ML service while staying small enough to finish, explain, and clean up safely.
