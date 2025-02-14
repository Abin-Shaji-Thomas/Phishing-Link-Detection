from flask import Flask, request, render_template
import pandas as pd
import pickle
import os
from utils.feature_extraction import extract_features

app = Flask(__name__)

# Load the trained model
MODEL_PATH = os.path.join('models', 'phishing_model.pkl')
model = pickle.load(open(MODEL_PATH, 'rb'))

# Load the data to get the column names
DATA_PATH = os.path.join('data', 'phishing_final.csv')
data = pd.read_csv(DATA_PATH)
X = data.drop('class', axis=1) # Drop the 'class' column to get feature names

def predict_phishing(url_features):
    """Predicts whether a URL is phishing or legitimate."""
    # Create a DataFrame from the input features
    input_df = pd.DataFrame([url_features], columns=X.columns)
    prediction = model.predict(input_df)[0]
    return "Phishing" if prediction == 1 else "Legitimate"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    url = request.form['url']

    # Extract features from the input URL
    url_features = extract_features(url)

    # Perform prediction
    prediction = predict_phishing(url_features)
    reason = ""

    if prediction == "Phishing":
        reason = "The URL has suspicious characteristics."
    else:
        reason = "The URL seems legitimate based on the features considered."

    return render_template('result.html', url=url, prediction=prediction, reason = reason)

if __name__ == '__main__':
    app.run(debug=True)
    