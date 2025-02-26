from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib
import re
from urllib.parse import urlparse
from feature_extractor import extract_features

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/check-url", methods=['POST'])
def predict_url():
    try:
        data = request.get_json()
        url = data.get("url")
        if not url:
            return jsonify({"error": "URL is required"}), 400

        features = extract_features(url)
        if not features:
            return jsonify({"error": "Failed to extract features from the URL"}), 400

        features_df = pd.DataFrame([features])
        print("Extracted Features:", features)  

        model = joblib.load('phishing_detection_model.pkl')
        prediction = model.predict(features_df)
        print("Prediction:", prediction)  

        return jsonify({"is_phishing": bool(prediction[0])})
    except Exception as e:
        print(f"Unexpected error: {e}")
        return jsonify({"error": "An unexpected error occurred"}), 500

if __name__ == "__main__":
    app.run(debug=True)