import mlflow
import numpy as np

# Path ke model (pastikan <run_id> benar)
model_uri = "mlruns/0/0cecf2f607ab4b99846abf76bedcb0fa/artifacts/logistic_regression_model"
loaded_model = mlflow.sklearn.load_model(model_uri)

def predict_class(feature1, feature2):
    input_data = np.array([[feature1, feature2]])
    prediction = loaded_model.predict(input_data)
    return prediction[0]

# Contoh penggunaan fungsi prediksi
feature_1 = 2.5
feature_2 = 3.7
predicted_class = predict_class(feature_1, feature_2)
print(f"Prediksi untuk fitur [{feature_1}, {feature_2}]: Kelas {predicted_class}")