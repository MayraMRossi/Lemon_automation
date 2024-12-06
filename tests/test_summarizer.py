import unittest
from unittest.mock import patch
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from infrastructure.nlp.summarizer import Summarizer
from utils.exceptions import SummarizationError

class TestSummarizer(unittest.TestCase):
    def setUp(self):
        self.summarizer = Summarizer()

    @patch('langchain_ollama.ChatOllama')
    def test_summarize(self, mock_chat_ollama):
        print("Testing summarize method...")
        mock_chat_ollama_instance = mock_chat_ollama.return_value
        mock_chat_ollama_instance.invoke.return_value = 'Summary of the message.'

        message = "This is a test message to summarize."
        summary = self.summarizer.summarize(message)

        self.assertEqual(summary, "Summary of the message.")
        print("summarize method test passed.")

    @patch('langchain_ollama.ChatOllama')
    def test_summarize_with_error(self, mock_chat_ollama):
        print("Testing summarize method with error...")
        mock_chat_ollama_instance = mock_chat_ollama.return_value
        mock_chat_ollama_instance.invoke.side_effect = Exception("Summarization error")

        message = "This is a test message to summarize."

        with self.assertRaises(SummarizationError):
            self.summarizer.summarize(message)
        print("summarize method with error test passed.")

if __name__ == "__main__":
    unittest.main()