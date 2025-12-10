from typing import Optional, List
from datetime import datetime

import mlflow
import mlflow.pyfunc
import pandas as pd
from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

# ---------- App & Model Versioning ----------
APP_VERSION = "0.1.0"
MODEL_NAME = "housing_price_model"

# Point MLflow to your local registry
mlflow.set_tracking_uri("file:./A2/mlruns")


# ---------- Pydantic Input Model ----------
class HousingFeatures(BaseModel):
    # These are the standard Boston Housing features
    CRIM: float = Field(..., ge=0, description="Per capita crime rate by town")
    ZN: float = Field(..., ge=0, description="Proportion of residential land zoned for lots over 25,000 sq.ft.")
    INDUS: float = Field(..., ge=0, description="Proportion of non-retail business acres per town")
    CHAS: int = Field(..., ge=0, le=1, description="Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)")
    NOX: float = Field(..., ge=0, description="Nitric oxides concentration (parts per 10 million)")
    RM: float = Field(..., ge=0, le=10, description="Average number of rooms per dwelling")
    AGE: float = Field(..., ge=0, le=100, description="Proportion of owner-occupied units built prior to 1940")
    DIS: float = Field(..., ge=0, description="Weighted distances to five Boston employment centres")
    RAD: float = Field(..., ge=0, description="Index of accessibility to radial highways")
    TAX: float = Field(..., ge=0, description="Full-value property-tax rate per $10,000")
    PTRATIO: float = Field(..., ge=0, description="Pupil-teacher ratio by town")
    B: float = Field(..., ge=0, description="1000(Bk - 0.63)^2 where Bk is the proportion of Black people by town")
    LSTAT: float = Field(..., ge=0, le=40, description="% lower status of the population")


# ---------- Helper to load model from MLflow ----------
def load_model(model_version: Optional[str] = None):
    """
    Load a model from MLflow Model Registry.

    If model_version is None, use 'latest'.
    Otherwise, use the specific version (e.g., '1').
    """
    if model_version:
        model_uri = f"models:/{MODEL_NAME}/{model_version}"
        used_version = model_version
    else:
        # 'latest' refers to latest version by stage/alias.
        # For this assignment it's fine to use 'latest' since we don't manage stages.
        model_uri = f"models:/{MODEL_NAME}/latest"
        used_version = "latest"

    model = mlflow.pyfunc.load_model(model_uri)
    return model, used_version


# ---------- FastAPI App ----------
app = FastAPI(
    title="Housing Price Prediction API",
    version=APP_VERSION,
    description="EE P 596 A2 – Housing model served from MLflow registry",
)


@app.post("/predict")
def predict(
    features: HousingFeatures,
    model_version: Optional[str] = Query(
        None, description="Optional model version to use (e.g. '1')"
    ),
):
    # Load model from registry
    model, used_version = load_model(model_version)

    # Build a DataFrame in the same column order as training
    data_dict = {
        "CRIM": [features.CRIM],
        "ZN": [features.ZN],
        "INDUS": [features.INDUS],
        "CHAS": [features.CHAS],
        "NOX": [features.NOX],
        "RM": [features.RM],
        "AGE": [features.AGE],
        "DIS": [features.DIS],
        "RAD": [features.RAD],
        "TAX": [features.TAX],
        "PTRATIO": [features.PTRATIO],
        "B": [features.B],
        "LSTAT": [features.LSTAT],
    }
    input_df = pd.DataFrame(data_dict)

    # Run prediction
    prediction = model.predict(input_df)[0]

    # Build response with metadata
    return {
        "prediction": prediction,
        "metadata": {
            "app_version": APP_VERSION,
            "model_version": used_version,
            "prediction_datetime": datetime.utcnow().isoformat(),
        },
    }


