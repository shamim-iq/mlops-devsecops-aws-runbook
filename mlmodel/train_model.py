from pathlib import Path

from app.main import MODEL_PATH, train_and_save_model


if __name__ == "__main__":
    model_path = Path(MODEL_PATH)
    train_and_save_model(model_path)
    print(f"Model trained and saved to {model_path}")
