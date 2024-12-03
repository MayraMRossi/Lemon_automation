from domain.models.intent_model import IntentInput, IntentOutput
from domain.repositories.intent_repository import IntentRepository
from infrastructure.nlp.classifier import Classifier

class IntentService:
    def __init__(self, repository: IntentRepository, classifier: Classifier):
        self.repository = repository
        self.classifier = classifier

    def classify_intent(self, question: IntentInput) -> IntentOutput:
        category = self.classifier.classify(question.question)
        return IntentOutput(intent=category, confidence=0.95)  # Mock confidence