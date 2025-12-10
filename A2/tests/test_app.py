import os
import sys


CURRENT_DIR = os.path.dirname(__file__)
REPO_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, "..", ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from fastapi.testclient import TestClient
from A2.main import app

client = TestClient(app)


def test_predict_happy_path():
    payload = {
        "CRIM": 0.1,
        "ZN": 18.0,
        "INDUS": 2.3,
        "CHAS": 0,
        "NOX": 0.5,
        "RM": 6.5,
        "AGE": 60.0,
        "DIS": 4.0,
        "RAD": 1.0,
        "TAX": 300.0,
        "PTRATIO": 15.0,
        "B": 396.0,
        "LSTAT": 5.0,
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "prediction" in data
    assert "metadata" in data
    assert data["metadata"]["app_version"] == "0.1.0"


def test_predict_missing_field():
    # Missing CRIM on purpose
    payload = {
        "ZN": 18.0,
        "INDUS": 2.3,
        "CHAS": 0,
        "NOX": 0.5,
        "RM": 6.5,
        "AGE": 60.0,
        "DIS": 4.0,
        "RAD": 1.0,
        "TAX": 300.0,
        "PTRATIO": 15.0,
        "B": 396.0,
        "LSTAT": 5.0,
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 422  # validation error