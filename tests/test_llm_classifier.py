import unittest
from unittest.mock import patch
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from infrastructure.nlp.llm_classifier import LlmClassifier
from utils.exceptions import ClassificationError

class TestLlmClassifier(unittest.TestCase):
    def setUp(self):
        self.classifier = LlmClassifier()

    @patch('langchain_ollama.ChatOllama')
    def test_classify(self, mock_chat_ollama):
        print("Testing classify method...")
        mock_chat_ollama_instance = mock_chat_ollama.return_value
        mock_chat_ollama_instance.invoke.return_value = 'Banking Queries'

        message = "This is a test email about banking"
        categories = {
            "Banking Queries": "Queries related to banking services.",
            "Crypto Queries": "Queries related to cryptocurrencies and their usage."
        }

        category = self.classifier.classify(message, categories)

        self.assertEqual(category, "Banking Queries")
        print("classify method test passed.")

    @patch('langchain_ollama.ChatOllama')
    def test_classify_with_error(self, mock_chat_ollama):
        print("Testing classify method with error...")
        mock_chat_ollama_instance = mock_chat_ollama.return_value
        mock_chat_ollama_instance.invoke.side_effect = Exception("Classification error")

        message = "This is a test email about banking"
        categories = {
            "Banking Queries": "Queries related to banking services.",
            "Crypto Queries": "Queries related to cryptocurrencies and their usage."
        }

        with self.assertRaises(ClassificationError):
            self.classifier.classify(message, categories)
        print("classify method with error test passed.")

if __name__ == "__main__":
    unittest.main()