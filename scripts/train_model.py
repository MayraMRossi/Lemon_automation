import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

# File paths
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
INTENTS_CSV_PATH = f'{root_path}\\app\\data\\intents.csv'
MODEL_PATH = f'{root_path}\\app\\models\\intent_classifier.pkl'
VECTORIZER_PATH = f'{root_path}\\app\\models\\tfidf_vectorizer.pkl'

# Create the directory if it doesn't exist
model_dir = os.path.dirname(MODEL_PATH)
if not os.path.exists(model_dir):
    os.makedirs(model_dir)

# 1. Load the dataset from the CSV file
df = pd.read_csv(INTENTS_CSV_PATH)

# 2. Text Preprocessing
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['question'])
y = df['category']

# 3. Train the Model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# 4. Evaluate the Model
y_pred = model.predict(X_test)
print("Classification Report:")
print(classification_report(y_test, y_pred))
print("Accuracy:", accuracy_score(y_test, y_pred))

# 5. Save the Model and the Vectorizer
joblib.dump(model, MODEL_PATH)
joblib.dump(vectorizer, VECTORIZER_PATH)

print(f"Model and vectorizer saved to {MODEL_PATH} and {VECTORIZER_PATH} respectively.")
