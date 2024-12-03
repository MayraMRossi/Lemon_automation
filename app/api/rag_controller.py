from flask import Blueprint, request, jsonify
from domain.services.rag_service import RAGService
from adapters.input.rag_input_adapter import RAGInputAdapter
from adapters.output.rag_output_adapter import RAGOutputAdapter
from infrastructure.persistence.rag_repository_impl import SQLAlchemyRAGRepository
from infrastructure.vector_store.vector_manager import VectorManager
from infrastructure.nlp.llm_integration import LLMIntegration

rag_blueprint = Blueprint("rag", __name__)
rag_service = RAGService(
    repository=SQLAlchemyRAGRepository(),
    vector_manager=VectorManager(),
    llm=LLMIntegration()
)

@rag_blueprint.route("/query", methods=["POST"])
def query_rag():
    try:
        input_adapter = RAGInputAdapter()
        output_adapter = RAGOutputAdapter()
        queries = input_adapter.read_queries("data/rag_data.json")
        processed_queries = [rag_service.query_rag(query) for query in queries]
        output_adapter.save_queries(processed_queries, "data/processed_queries.json")
        return jsonify({"message": "Queries processed successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500