# ML Model Demo

This folder contains a minimal machine learning application matching the project direction in the runbook: a small scikit-learn model trained on the Iris dataset and exposed through a FastAPI service. The app is intentionally lightweight so it can be used as a local prototype before deploying to ECR and EKS.

## What it does

- Trains a logistic regression model on the built-in Iris dataset
- Saves the trained artifact to `app/model/model.pkl`
- Exposes `/health`, `/metrics`, and `/predict` endpoints
- Can be tested locally with `pytest`

## Run it

```bash
python -m pip install -r requirements.txt
python train_model.py
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Then call:

```bash
curl http://localhost:8000/health
curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
```
