# Model API Container Build

This project builds the application artifact for the MLOps demo. It creates a lightweight scikit-learn model saved as `model.pkl`, serves predictions through FastAPI, adds local quality checks, and containerizes the API so it can be pushed to Amazon ECR later.

## Owner

Project owner - implementation repository `<implementation-repository-url>`.

## Status

`active` - 2026-08-22. The FastAPI service now loads `app/model/model.pkl` for `/predict`. `scripts/train_model.py` trains Logistic Regression on the built-in scikit-learn Iris dataset and writes the artifact. Python 3.12.8 is installed, dependencies are installed in `.venv`, and `pytest` passes with 3 tests. Linting, dependency check, and container verification are not created yet.

## Application Shape

```text
<repo-root>/
|-- app/
|   |-- main.py
|   |-- model/
|   |   `-- model.pkl
|-- tests/
|   `-- test_health.py
|-- requirements.txt
|-- Dockerfile
`-- README.md
```

The API exposes health, prediction, and metrics endpoints. `/predict` loads the serialized scikit-learn artifact at startup and returns the predicted class with the highest class probability as the score.

The model uses the built-in scikit-learn Iris dataset and Logistic Regression. This keeps the demo CPU-only, avoids external data handling, and creates a familiar classification prediction that is easy to explain in a CV or interview walkthrough. The training script writes `app/model/model.pkl`, and the Docker image will include the artifact because it lives under `app/`.

> [CONFIRM] Linting tool, dependency checker, and final Prometheus metric thresholds are not finalized yet.

## Next

1. Add linting and dependency checks.
2. Build and run the container locally.
3. Verify the health, prediction, and metrics endpoints from the running container.
4. Record the container verification output.

## Files

| File | What you'd learn there |
|---|---|
| [Progress.md](./Progress.md) | Application build work completed and remaining |
| [checklist.md](./checklist.md) | Model, API, tests, quality checks, and Docker decisions |
