import mlflow
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

# Contoh data klasifikasi sederhana
X = np.array([[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]])
y = np.array([0, 0, 1, 1, 0, 1])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

with mlflow.start_run(run_name="Simple Logistic Regression"):
    solver = "liblinear"
    random_state = 20

    mlflow.log_param("solver", solver)
    mlflow.log_param("random_state", random_state)

    model = LogisticRegression(solver=solver, random_state=random_state)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    mlflow.log_metric("accuracy", accuracy)

    mlflow.sklearn.log_model(model, "logistic_regression_model")

print("MLflow run completed. Open MLflow UI to view the results.")
print("Run 'mlflow ui' in your terminal to start the UI.")