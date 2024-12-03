from domain.models.rag_model import RAGQueryInput, RAGQueryOutput
from domain.repositories.rag_repository import RAGRepository
from infrastructure.vector_store.vector_manager import VectorManager
from infrastructure.nlp.llm_integration import LLMIntegration

class RAGService:
    def __init__(self, repository: RAGRepository, vector_manager: VectorManager, llm: LLMIntegration):
        self.repository = repository
        self.vector_manager = vector_manager
        self.llm = llm

    def query_rag(self, query: RAGQueryInput) -> RAGQueryOutput:
        result = self.vector_manager.search_vectors(query.query)
        response = self.llm.generate_response(query.query, result["context"])
        return RAGQueryOutput(answer=response, context=result["context"])