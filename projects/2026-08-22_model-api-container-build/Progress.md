# Model API Container Build Progress

## Current State

`active` - 2026-08-22. The FastAPI app loads `app/model/model.pkl` for `/predict`. `scripts/train_model.py` trains Logistic Regression on the built-in scikit-learn Iris dataset and writes the artifact. Python 3.12.8 is installed, dependencies are installed in `.venv`, and `pytest` passes with 3 tests. Docker builds `mlops-prediction-api:local`, the container runs, and health, prediction, and metrics endpoints are verified. `ruff` and `pip-audit` pass locally, and the CI workflow runs tests, linting, dependency audit, then Docker build.

## Done

- [x] Record requirement to build a lightweight scikit-learn model.
- [x] Record required model artifact name: `model.pkl`.
- [x] Record requirement for FastAPI health and metrics endpoints.
- [x] Record requirement for unit tests, linting, dependency checks, and local run commands.
- [x] Record requirement to containerize the API with Docker.
- [x] Define prediction request and response schema.
- [x] Create FastAPI app.
- [x] Add health endpoint.
- [x] Add prediction endpoint with deterministic baseline logic.
- [x] Add metrics endpoint.
- [x] Add first pytest tests.
- [x] Add documented local run commands.
- [x] Create Dockerfile.
- [x] Install Python 3.12.8 and create project `.venv`.
- [x] Install Python dependencies.
- [x] Run unit tests: 3 passed.
- [x] Choose dataset: built-in scikit-learn Iris dataset.
- [x] Choose final model type: Logistic Regression.
- [x] Create model training script: `scripts/train_model.py`.
- [x] Save trained artifact as `app/model/model.pkl`.
- [x] Replace deterministic baseline with artifact-backed prediction.
- [x] Add prediction response checks for artifact-backed output.
- [x] Run unit tests after model integration: 3 passed.
- [x] Build Docker image locally: `mlops-prediction-api:local`.
- [x] Run Docker container locally on port `8000`.
- [x] Verify container health endpoint: `{"status":"ok"}`.
- [x] Verify container prediction endpoint returns `model_version` `iris-logreg-0.1.0`.
- [x] Verify container metrics endpoint exposes `/predict` request count and prediction latency.
- [x] Add linting command: `ruff check app scripts tests`.
- [x] Add dependency check command: `pip-audit -r requirements-dev.txt`.
- [x] Split runtime and development dependencies.
- [x] Add CI workflow with tests, linting, dependency audit, then Docker build.
- [x] Run linting locally: passed.
- [x] Run dependency audit locally: no known vulnerabilities found.
- [x] Rebuild Docker image after dependency changes.
- [x] Smoke test rebuilt container health, prediction, and metrics endpoints.
- [x] Document prediction app functionality and training flow.

## Remaining

- [ ] Commit and push linting, dependency audit, and CI workflow changes.
- [ ] Open or update the implementation pull request.
- [ ] Merge after review.
