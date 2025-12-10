import mlflow
import mlflow.sklearn
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_diabetes

# Use local file-based tracking inside A2
mlflow.set_tracking_uri("file:./A2/mlruns")
mlflow.set_experiment("my-first-experiment")

# Tiny demo model
X, y = load_diabetes(return_X_y=True)
model = LinearRegression().fit(X, y)

with mlflow.start_run():
    mlflow.log_param("model_type", "LinearRegression")
    mlflow.sklearn.log_model(
        sk_model=model,
        artifact_path="model",
        registered_model_name="diabetes-model",
    )

print("Run complete! Check MLflow UI for 'diabetes-model'.")


