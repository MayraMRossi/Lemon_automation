import unittest
from unittest.mock import patch
from flask import Flask
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from api.rag_controller import rag_blueprint, query_rag
from utils.exceptions import RAGQueryError

class TestRAGController(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(rag_blueprint)
        self.client = self.app.test_client()

    @patch('api.rag_controller.RAGService')
    def test_query_rag(self, mock_rag_service):
        print("Testing query_rag endpoint...")
        mock_rag_service_instance = mock_rag_service.return_value
        mock_rag_service_instance.query_rag.return_value = {"answer": "Test answer", "context": "Test context", "urls": ["http://example.com"]}

        response = self.client.post('/rag/query', json={"query": "Test query"})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"answer": "Test answer", "context": "Test context", "urls": ["http://example.com"]})
        print("query_rag endpoint test passed.")

    @patch('api.rag_controller.RAGService')
    def test_query_rag_with_error(self, mock_rag_service):
        print("Testing query_rag endpoint with error...")
        mock_rag_service_instance = mock_rag_service.return_value
        mock_rag_service_instance.query_rag.side_effect = RAGQueryError("Query error")

        response = self.client.post('/rag/query', json={"query": "Test query"})

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {"error": "Error querying RAG service: Query error"})
        print("query_rag endpoint with error test passed.")

if __name__ == "__main__":
    unittest.main()