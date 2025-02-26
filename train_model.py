import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

data = pd.read_csv('datasets/url_dataset_with_features.csv')

X = data[['url_length', 'num_special_chars', 'has_ip', 'domain_length', 'num_subdomains', 'domain_age', 'has_suspicious_keyword']]
y = data['label']  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(random_state=42)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

joblib.dump(model, 'phishing_detection_model.pkl')
print("Model saved as 'phishing_detection_model.pkl'")