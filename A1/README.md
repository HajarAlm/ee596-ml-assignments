# EE596 A1 – Housing Price Prediction API

This project deploys the linear regression model from **A0** as a REST API.

- **Framework:** FastAPI  
- **Model:** scikit-learn pipeline (StandardScaler + LinearRegression)  
- **Task:** Predict Boston Housing `MEDV` (median house value in \$1000s)

---

## Deployed API (AWS EC2)
The application is running on an EC2 instance in us-east-2 (Ohio).
- Base URL: http://3.129.17.233
- Docs (Swagger UI): http://3.129.17.233/docs

Example request body:
```json
{
  "CRIM": 0.1,
  "ZN": 18.0,
  "INDUS": 2.3,
  "CHAS": 0,
  "NOX": 0.45,
  "RM": 6.3,
  "AGE": 45.0,
  "DIS": 5.0,
  "RAD": 1,
  "TAX": 300.0,
  "PTRATIO": 15.0,
  "B": 396.0,
  "LSTAT": 5.0
}
```

Example response:
```json
{
  "prediction": 29.255944678375336
}
```
(≈ $292,559 predicted median house value.)

## Project Structure

```text
A1/
  app/
    __init__.py
    main.py          # FastAPI app / endpoints
    model_utils.py   # loads model.joblib and wraps prediction
  model/
    train_model.ipynb  # training notebook from A0
    model.joblib       # saved sklearn pipeline
  Dockerfile
  requirements.txt
  deploy_notes.md
  README.md
```
