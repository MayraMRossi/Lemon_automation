import unittest
from app.domain.services.intent_service import IntentService
from app.domain.models.intent_model import IntentInput, IntentOutput
from app.infrastructure.nlp.classifier import Classifier

class TestIntentService(unittest.TestCase):
    def setUp(self):
        self.service = IntentService(
            repository=MockIntentRepository(),
            classifier=Classifier()
        )

    def test_classify_intent(self):
        intent = IntentInput(question="How to withdraw crypto?")
        result = self.service.classify_intent(intent)
        self.assertEqual(result.intent, "Crypto")

class MockIntentRepository:
    def save_intents(self, intents):
        pass

if __name__ == "__main__":
    unittest.main()