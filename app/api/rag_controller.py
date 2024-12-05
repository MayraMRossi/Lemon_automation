from flask import Blueprint, request, jsonify
from domain.services.rag_service import RAGService

rag_blueprint = Blueprint("rag", __name__)
rag_service = RAGService()

@rag_blueprint.route("/query", methods=["POST"])
def query_rag():
    try:
        data = request.json
        query = data.get('query')
        if not query:
            return jsonify({'error': 'Query is required'}), 400

        response = rag_service.query_rag(query)
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500