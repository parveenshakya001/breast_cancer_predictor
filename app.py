import os
import joblib
import numpy as np
from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model

app = Flask(__name__)

# --- Load model and scaler once at startup ---
MODEL_PATH = "breast_cancer_model.h5"
SCALER_PATH = "breast_cancer_scaler.pkl"

model = load_model(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

# Must match the exact order of data.feature_names from sklearn's load_breast_cancer()
FEATURE_NAMES = [
    "mean radius", "mean texture", "mean perimeter", "mean area",
    "mean smoothness", "mean compactness", "mean concavity",
    "mean concave points", "mean symmetry", "mean fractal dimension",
    "radius error", "texture error", "perimeter error", "area error",
    "smoothness error", "compactness error", "concavity error",
    "concave points error", "symmetry error", "fractal dimension error",
    "worst radius", "worst texture", "worst perimeter", "worst area",
    "worst smoothness", "worst compactness", "worst concavity",
    "worst concave points", "worst symmetry", "worst fractal dimension",
]


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Breast Cancer Prediction API is running.",
        "usage": "POST /predict with JSON body: {'features': [30 numeric values in the correct order]}"
    })


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json(force=True)

        if "features" not in data:
            return jsonify({"error": "Missing 'features' key in request body"}), 400

        features = data["features"]

        if len(features) != 30:
            return jsonify({
                "error": f"Expected 30 features, got {len(features)}",
                "expected_order": FEATURE_NAMES
            }), 400

        # Reshape and scale exactly like during training
        input_array = np.array(features, dtype=float).reshape(1, -1)
        input_scaled = scaler.transform(input_array)

        prediction = model.predict(input_scaled, verbose=0)
        probability = float(prediction[0][0])
        diagnosis = "Malignant risk (1)" if probability > 0.5 else "Benign risk (0)"

        return jsonify({
            "probability": probability,
            "prediction": diagnosis
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    # Render sets the PORT environment variable automatically
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
