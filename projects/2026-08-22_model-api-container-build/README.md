# Model API Container Build

This project builds the application artifact for the MLOps demo. It creates a lightweight scikit-learn model saved as `model.pkl`, serves predictions through FastAPI, adds local quality checks, and containerizes the API so it can be pushed to Amazon ECR later.

## Owner

shamim.linkedin@gmail.com - source repository `https://github.com/shamim-iq/mlops-devsecops-aws-runbook.git`.

## Status

`active` - 2026-08-22. The application build scope is recorded. No model artifact, FastAPI service, tests, linting setup, dependency checks, Dockerfile, or local container verification has been created yet.

## Application Shape

```text
<repo-root>/
|-- app/
|   |-- main.py
|   |-- model/
|   |   `-- model.pkl
|   `-- schemas.py
|-- tests/
|   |-- test_health.py
|   `-- test_predict.py
|-- requirements.txt
|-- Dockerfile
`-- README.md
```

The API exposes health, prediction, and metrics endpoints. The model stays intentionally small so the demo remains CPU-only, fast to build, and easy to explain.

> [CONFIRM] Dataset choice, model type, prediction schema, metric names, linting tool, dependency checker, and local run commands are not finalized yet.

## Next

1. Choose the small demonstration dataset and model type.
2. Create the training script or artifact-generation step that writes `model.pkl`.
3. Build the FastAPI app with health, prediction, and metrics endpoints.
4. Add unit tests for health and prediction behavior.
5. Add linting and dependency checks.
6. Add documented local run commands.
7. Create the Dockerfile.
8. Build and run the container locally.
9. Verify the health, prediction, and metrics endpoints from the running container.

## Files

| File | What you'd learn there |
|---|---|
| [Progress.md](./Progress.md) | Application build work completed and remaining |
| [checklist.md](./checklist.md) | Model, API, tests, quality checks, and Docker decisions |
