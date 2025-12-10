from fastapi import FastAPI
from pydantic import BaseModel
from .model_utils import predict_from_features

app = FastAPI(title="EE596 A1 – Housing Price API")


# Input schema must match the features used in training (Boston Housing)
class HouseFeatures(BaseModel):
    CRIM: float
    ZN: float
    INDUS: float
    CHAS: float   # 0 or 1, but float is fine
    NOX: float
    RM: float
    AGE: float
    DIS: float
    RAD: float
    TAX: float
    PTRATIO: float
    B: float
    LSTAT: float


@app.get("/")
def root():
    return {"message": "Housing model API is running."}


@app.post("/predict")
def predict(features: HouseFeatures):
    # Order MUST match the training data column order:
    # CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT
    feature_list = [
        features.CRIM,
        features.ZN,
        features.INDUS,
        features.CHAS,
        features.NOX,
        features.RM,
        features.AGE,
        features.DIS,
        features.RAD,
        features.TAX,
        features.PTRATIO,
        features.B,
        features.LSTAT,
    ]

    prediction = predict_from_features(feature_list)
    return {"prediction": prediction}
