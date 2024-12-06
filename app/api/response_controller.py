from flask import Blueprint, request, jsonify
from domain.services.intent_service import IntentService
from domain.services.rag_service import RAGService
from infrastructure.nlp.llm_integration import LLMIntegration
from utils.exceptions import IntentClassificationError, RAGQueryError
import json

response_blueprint = Blueprint("response", __name__)
intent_service = IntentService()
rag_service = RAGService()
llm_integration = LLMIntegration()

# Load standard responses from a JSON file
with open('app/data/standard_responses.json', 'r') as file:
    standard_responses = json.load(file)

@response_blueprint.route("/get_response", methods=["POST"])
def get_response():
    """
    Endpoint to get a response based on the intent classification.
    If the intent is categorized (not "Other"), it uses a standard response and passes it through Ollama.
    If the intent is "Other", it queries the RAG system.

    Returns:
        JSON: A JSON response with the generated answer or an error message.
    """
    try:
        data = request.json
        question = data.get('question')
        if not question:
            return jsonify({'error': 'Question is required'}), 400

        # Classify the intent
        category = intent_service.classify_question(question)
        print(category)

        if category != "Otro":
            # Use a standard response for categorized intents
            standard_response = standard_responses.get(category, "No standard response available.")
            # Pass the standard response through Ollama
            personalized_response = llm_integration.generate_response(query=question, context=standard_response)
            return jsonify({'answer': personalized_response})
        else:
            # Query the RAG system for "Other" intents
            rag_response = rag_service.query_rag(question)
            return jsonify(rag_response)

    except Exception as e:
        raise IntentClassificationError(f"Error getting response: {str(e)}")