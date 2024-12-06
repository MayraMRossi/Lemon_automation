import unittest
from unittest.mock import patch
from flask import Flask
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from api.intent_controller import intent_blueprint, classify_intent
from utils.exceptions import IntentClassificationError

class TestIntentController(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(intent_blueprint)
        self.client = self.app.test_client()

    @patch('api.intent_controller.IntentService')
    def test_classify_intent(self, mock_intent_service):
        print("Testing classify_intent endpoint...")
        mock_intent_service_instance = mock_intent_service.return_value
        mock_intent_service_instance.classify_question.return_value = "Retiros Crypto"

        response = self.client.post('/intents/classify', json={"question": "¿Cómo retiro mis fondos en criptomonedas?"})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"category": "Retiros Crypto"})
        print("classify_intent endpoint test passed.")

    @patch('api.intent_controller.IntentService')
    def test_classify_intent_with_error(self, mock_intent_service):
        print("Testing classify_intent endpoint with error...")
        mock_intent_service_instance = mock_intent_service.return_value
        mock_intent_service_instance.classify_question.side_effect = IntentClassificationError("Classification error")

        response = self.client.post('/intents/classify', json={"question": "¿Cómo retiro mis fondos en criptomonedas?"})

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {"error": "Error classifying intent: Classification error"})
        print("classify_intent endpoint with error test passed.")

if __name__ == "__main__":
    unittest.main()