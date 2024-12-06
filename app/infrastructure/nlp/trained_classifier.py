import os

import joblib
from utils.exceptions import ModelLoadingError
from utils.exceptions import ClassificationError


class TrainedClassifier:
    """A classifier trained on a specific model and vectorizer."""

    def __init__(self, model_path, vectorizer_path):
        try:
            self.model = joblib.load(model_path)
            self.vectorizer = joblib.load(vectorizer_path)
        except Exception as e:
            raise ModelLoadingError(f"Error loading trained classifier: {str(e)}")

    def classify(self, question: str) -> str:
        """
        Classifies the intent of a user's question.

        Args:
            question (str): The user's question.

        Returns:
            str: The classified intent category.
        """
        try:
            question_vector = self.vectorizer.transform([question])
            category = self.model.predict(question_vector)
            return category[0]
        except Exception as e:
            raise ClassificationError(f"Error classifying question: {str(e)}")