from pathlib import Path
import joblib
import numpy as np

# Path to model.joblib (../model/model.joblib)
MODEL_PATH = Path(__file__).resolve().parents[1] / "model" / "model.joblib"

# Load model once at import time
model = joblib.load(MODEL_PATH)

def predict_from_features(features: list[float]) -> float:
    """Take a list of numeric features in the SAME ORDER used at training
    and return a single prediction."""
    X = np.array(features).reshape(1, -1)
    y_pred = model.predict(X)[0]
    return float(y_pred)