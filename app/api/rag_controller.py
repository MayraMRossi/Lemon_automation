from flask import Blueprint, request, jsonify
from domain.services.rag_service import RAGService
from utils.exceptions import RAGQueryError

rag_blueprint = Blueprint("rag", __name__)
rag_service = RAGService()

@rag_blueprint.route("/query", methods=["POST"])
def query_rag():
    """
    Endpoint to query the RAG service.
    ---
    parameters:
      - name: query
        in: body
        type: string
        required: true
        description: The query to be processed by the RAG service
    responses:
      200:
        description: Successfully processed the query and returned the response
        examples:
          application/json: {"response": "The generated answer based on the query"}
      400:
        description: Bad request, missing query
        examples:
          application/json: {"error": "Query is required"}
      500:
        description: Internal server error
        examples:
          application/json: {"error": "Error querying RAG service: <error details>"}
    """
    try:
        data = request.json
        query = data.get('query')
        if not query:
            return jsonify({'error': 'Query is required'}), 400

        response = rag_service.query_rag(query)
        return jsonify(response)
    except Exception as e:
        raise RAGQueryError(f"Error querying RAG service: {str(e)}")