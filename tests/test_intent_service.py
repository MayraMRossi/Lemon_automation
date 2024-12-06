import unittest
from unittest.mock import patch
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from domain.services.intent_service import IntentService

class TestIntentService(unittest.TestCase):
    def setUp(self):
        self.service = IntentService()

    @patch('app.domain.services.intent_service.TrainedClassifier')
    def test_classify_question(self, mock_classifier):
        print("Testing classify_question method...")
        mock_classifier_instance = mock_classifier.return_value
        mock_classifier_instance.classify.return_value = "Retiros Crypto"

        question = "¿Cómo retiro mis fondos en criptomonedas?"
        category = self.service.classify_question(question)

        self.assertEqual(category, "Retiros Crypto")
        print("classify_question method test passed.")

if __name__ == "__main__":
    unittest.main()