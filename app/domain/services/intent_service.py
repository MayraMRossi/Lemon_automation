from domain.models.intent_model import IntentInput, IntentOutput
from domain.repositories.intent_repository import IntentRepository
from infrastructure.nlp.trained_classifier import TrainedClassifier

class IntentService:
    def __init__(self):
        self.classifier = TrainedClassifier(model_path='app/models/intent_classifier.pkl', vectorizer_path='app/models/tfidf_vectorizer.pkl')

    def classify_question(self, question):
        return self.classifier.classify(question)