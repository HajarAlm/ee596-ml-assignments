# A0 – Housing Price Prediction

I followed a tutorial to build a linear regression model on the **Boston Housing** dataset in **Google Colab**, then downloaded the notebook into this folder.

Notebook: `a0_housing_regression.ipynb`

---

## What I did

- Loaded the Boston Housing dataset into pandas and selected `MEDV` as the target.
- Split the data into train/test sets.
- Implemented linear regression from scratch (cost, gradient, gradient descent).
- Trained and evaluated the model (MSE, predicted vs. actual plots).
- Standardized features with `StandardScaler` and retrained to compare performance.

---

## What was easy

- Running code and managing packages in Colab.
- Using scikit-learn for splitting and scaling.

---

## What was hard

- Getting the gradient descent math and array shapes correct.
- Choosing a learning rate that made the cost decrease.

---

## Where I got stuck & resources

- Minor issues with file paths/filenames when loading the dataset.
- I used the provided tutorial, scikit-learn docs, and ChatGPT to resolve questions.

