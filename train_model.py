import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle  # To save the trained model
import os

# Load your CSV data
DATA_PATH = os.path.join('data', 'phishing_final.csv')  # Construct the path
data = pd.read_csv(DATA_PATH)

# Data Cleaning and Preprocessing
data = data.fillna(data.mode().iloc[0])  # Handle NaN values by filling with the mode
data = data.drop('Index', axis=1, errors='ignore')  # Drop index column
X = data.drop('class', axis=1)
y = data['class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Training (Random Forest)
model = RandomForestClassifier(random_state=42)  # RandomForest is generally more robust
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

# Save the trained model
MODEL_PATH = os.path.join('models', 'phishing_model.pkl')
os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True) # Ensure the directory exists
pickle.dump(model, open(MODEL_PATH, 'wb'))

print(f"Trained model saved to {MODEL_PATH}")
