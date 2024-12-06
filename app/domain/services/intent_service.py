from infrastructure.nlp.trained_classifier import TrainedClassifier
from utils.constants import INTENT_CLASSIFIER_MODEL_PATH, TFIDF_VECTORIZER_PATH
from utils.exceptions import IntentClassificationError

from utils.exceptions import ModelLoadingError


class IntentService:
    """Service to classify the intent of a user's question."""

    def __init__(self):
        try:
            self.classifier = TrainedClassifier(model_path=INTENT_CLASSIFIER_MODEL_PATH, vectorizer_path=TFIDF_VECTORIZER_PATH)
        except Exception as e:
            raise ModelLoadingError(f"Error loading intent classifier model: {str(e)}")

    def classify_question(self, question: str) -> str:
        """
        Classifies the intent of a user's question.

        Args:
            question (str): The user's question.

        Returns:
            str: The classified intent category.
        """
        try:
            return self.classifier.classify(question)
        except Exception as e:
            raise IntentClassificationError(f"Error classifying intent: {str(e)}")