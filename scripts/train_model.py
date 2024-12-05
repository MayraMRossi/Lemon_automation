import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Paths de los archivos
INTENTS_CSV_PATH = 'data/intents.csv'
MODEL_PATH = 'app/models/intent_classifier.pkl'
VECTORIZER_PATH = 'app/models/tfidf_vectorizer.pkl'

# 1. Cargar el dataset desde el archivo CSV
df = pd.read_csv(INTENTS_CSV_PATH)

# 2. Preprocesamiento de Texto
# Crear el vectorizador TF-IDF
vectorizer = TfidfVectorizer()

# Transformar las preguntas en vectores TF-IDF
X = vectorizer.fit_transform(df['question'])

# Obtener las etiquetas de las categorías
y = df['category']

# 3. Entrenar el Modelo
# Dividir el dataset en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar un modelo de árboles de decisión
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# 4. Evaluar el Modelo
# Predecir las categorías para el conjunto de prueba
y_pred = model.predict(X_test)

# Mostrar el reporte de clasificación y la precisión
print("Classification Report:")
print(classification_report(y_test, y_pred))
print("Accuracy:", accuracy_score(y_test, y_pred))

# 5. Guardar el Modelo y el Vectorizador
# Guardar el modelo entrenado
joblib.dump(model, MODEL_PATH)

# Guardar el vectorizador TF-IDF
joblib.dump(vectorizer, VECTORIZER_PATH)

print(f"Modelo y vectorizador guardados en {MODEL_PATH} y {VECTORIZER_PATH} respectivamente.")