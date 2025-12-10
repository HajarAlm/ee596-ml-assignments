# EE596 A1 – Housing Price Prediction API

This project deploys the linear regression model from **A0** as a REST API.

- **Framework:** FastAPI  
- **Model:** scikit-learn pipeline (StandardScaler + LinearRegression)  
- **Task:** Predict Boston Housing `MEDV` (median house value in \$1000s)

---

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
