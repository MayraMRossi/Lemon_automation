import unittest
from app.domain.services.rag_service import RAGService
from app.domain.models.rag_model import RAGQueryInput, RAGQueryOutput
from app.infrastructure.vector_store.vector_manager import VectorManager
from app.infrastructure.nlp.llm_integration import LLMIntegration

class TestRAGService(unittest.TestCase):
    def setUp(self):
        self.service = RAGService(
            repository=MockRAGRepository(),
            vector_manager=VectorManager(),
            llm=LLMIntegration()
        )

    def test_query_rag(self):
        query = RAGQueryInput(query="What is Lemon Earn?")
        result = self.service.query_rag(query)
        self.assertIsInstance(result, RAGQueryOutput)

class MockRAGRepository:
    def save_queries(self, queries):
        pass

if __name__ == "__main__":
    unittest.main()