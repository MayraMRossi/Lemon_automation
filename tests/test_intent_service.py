import unittest
from domain.services.intent_service import IntentService

class TestIntentService(unittest.TestCase):
    def setUp(self):
        self.service = IntentService()

    def test_classify_question(self):
        question = "¿Cómo retiro mis fondos en criptomonedas?"
        category = self.service.classify_question(question)
        self.assertEqual(category, "Retiros Crypto")

if __name__ == "__main__":
    unittest.main()