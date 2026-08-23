from __future__ import annotations

import pickle
from pathlib import Path

import numpy as np
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

MODEL_DIR = Path(__file__).resolve().parent / "model"
MODEL_PATH = MODEL_DIR / "model.pkl"

app = FastAPI(title="Iris ML API", version="0.1.0")


def train_and_save_model(output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    X, y = load_iris(return_X_y=True)
    model = LogisticRegression(max_iter=200, random_state=42)
    model.fit(X, y)

    with output_path.open("wb") as f:
        pickle.dump(model, f)

    return output_path


def load_model() -> LogisticRegression:
    if not MODEL_PATH.exists():
        train_and_save_model(MODEL_PATH)

    with MODEL_PATH.open("rb") as f:
        return pickle.load(f)


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "model": str(MODEL_PATH.name)}


@app.get("/metrics")
def metrics() -> dict:
    return {
        "model": "iris-logistic-regression",
        "version": "0.1.0",
        "status": "healthy",
    }


@app.post("/predict")
def predict(payload: dict) -> JSONResponse:
    try:
        features = payload.get("features")
        if not isinstance(features, list) or len(features) != 4:
            return JSONResponse(
                status_code=400,
                detail="Provide four feature values in the 'features' list.",
            )

        model = load_model()
        sample = np.asarray([features], dtype=float)
        prediction = int(model.predict(sample)[0])
        probabilities = model.predict_proba(sample)[0]
        top_index = int(np.argmax(probabilities))
        score = float(probabilities[top_index])

        return JSONResponse(
            content={
                "prediction": prediction,
                "class_label": model.classes_[prediction].item() if hasattr(model.classes_[prediction], "item") else model.classes_[prediction],
                "confidence": round(score, 4),
                "probabilities": {str(label): round(float(prob), 4) for label, prob in zip(model.classes_, probabilities)},
            }
        )
    except Exception as exc:  # pragma: no cover - surfaced as API error
        return JSONResponse(status_code=500, content={"error": str(exc)})
