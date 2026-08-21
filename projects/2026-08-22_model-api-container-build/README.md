# Model API Container Build

This project builds the application artifact for the MLOps demo. It creates a lightweight scikit-learn model saved as `model.pkl`, serves predictions through FastAPI, adds local quality checks, and containerizes the API so it can be pushed to Amazon ECR later.

## Owner

Project owner - implementation repository `<implementation-repository-url>`.

## Status

`active` - 2026-08-22. The initial FastAPI service, health endpoint, prediction endpoint, metrics endpoint, first tests, dependency file, Dockerfile, and local run commands are created in `<local-implementation-repo>`. Python 3.12.8 is installed, dependencies are installed in `.venv`, and `pytest` passes. The scikit-learn `model.pkl`, training step, linting, dependency check, and container verification are not created yet.

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

The API exposes health, prediction, and metrics endpoints. The current prediction logic is a deterministic baseline so API, metrics, tests, and container work can start before the scikit-learn artifact exists. The model stays intentionally small so the demo remains CPU-only, fast to build, and easy to explain.

> [CONFIRM] Dataset choice, model type, linting tool, dependency checker, and final Prometheus metric thresholds are not finalized yet.

## Next

1. Choose the small demonstration dataset and model type.
2. Create the training script or artifact-generation step that writes `app/model/model.pkl`.
3. Replace the deterministic baseline with artifact-backed prediction.
4. Add linting and dependency checks.
5. Build and run the container locally.
6. Verify the health, prediction, and metrics endpoints from the running container.

## Files

| File | What you'd learn there |
|---|---|
| [Progress.md](./Progress.md) | Application build work completed and remaining |
| [checklist.md](./checklist.md) | Model, API, tests, quality checks, and Docker decisions |
