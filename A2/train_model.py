import mlflow
import mlflow.sklearn

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Use the same local MLflow setup as before
mlflow.set_tracking_uri("file:./A2/mlruns")
mlflow.set_experiment("housing-a2")

MODEL_NAME = "housing_price_model"


def train_and_register():
    # 1. Load the Boston Housing data (same as A0)
    # NOTE: this assumes Boston_Housing.xlsx is in the repo root
    data = pd.read_excel("Boston_Housing.xlsx")

    # 2. Split into features (X) and target (y)
    y = data["MEDV"]
    X = data.drop(columns=["MEDV"])

    # 3. Train/test split (same as A0)
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
    )

# 4. Build the pipeline (StandardScaler + LinearRegression)
    model = make_pipeline(
        StandardScaler(),
        LinearRegression(),
    )

    # 5. Fit the model
    model.fit(X_train, y_train)

    # 6. Evaluate on test set (optional, but good to log)
    y_pred = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    print(f"Test RMSE: {rmse:.3f}")

    # 7. Log & register the model in MLflow
    with mlflow.start_run():
        mlflow.log_param("model_type", "StandardScaler+LinearRegression")
        mlflow.log_metric("rmse", rmse)

        mlflow.sklearn.log_model(
            sk_model=model,
            artifact_path="model",
            registered_model_name=MODEL_NAME,
        )

    print(f"Finished training + registering '{MODEL_NAME}'")


if __name__ == "__main__":
    train_and_register()

