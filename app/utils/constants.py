import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Email Categories
EMAIL_CATEGORIES = {
    "Crypto Queries": "Queries related to cryptocurrencies and their usage.",
    "Banking Queries": "Queries related to banking services.",
    "Card Queries": "Queries related to credit and debit cards.",
    "Other": "Any other query that does not fit into the above categories."
}

# File Paths
EMAILS_CSV_PATH = f"{ROOT_DIR}/data/emails.csv"
PROCESSED_EMAILS_CSV_PATH = f"{ROOT_DIR}/data/processed_emails.csv"

# Model Paths
INTENT_CLASSIFIER_MODEL_PATH = f"{ROOT_DIR}/models/intent_classifier.pkl"
TFIDF_VECTORIZER_PATH = f"{ROOT_DIR}/models/tfidf_vectorizer.pkl"

# Vector Store Path
VECTOR_STORE_PATH = "app/data/vector_store"

# Collection Name
VECTOR_STORE_COLLECTION_NAME = "help_center"

# Query Top K
QUERY_TOP_K = 5