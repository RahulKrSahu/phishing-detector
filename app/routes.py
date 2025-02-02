from flask import request, jsonify, render_template
from app import app  
import joblib
from app.utils.feature_extractor import extract_features
import os

# MODEL_PATH = os.path.join('app', 'models', 'phishing_detection_model.pkl')
# model = joblib.load(MODEL_PATH)

@app.route('/check-url', methods=['POST'])
def check_url():
    data = request.json
    url = data.get('url')

    if not url:
        return jsonify({"error": "URL is required"}), 400

    try:
        features = extract_features(url)
        prediction = model.predict([features])
        is_phishing = bool(prediction[0])

        return jsonify({"url": url, "is_phishing": is_phishing})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def home():
    return render_template('index.html')