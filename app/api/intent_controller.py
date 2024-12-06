from flask import Blueprint, request, jsonify
from domain.services.intent_service import IntentService
from utils.exceptions import IntentClassificationError

intent_blueprint = Blueprint("intent", __name__)
intent_service = IntentService()

@intent_blueprint.route("/classify", methods=["POST"])
def classify_intent():
    """
    Endpoint to classify the intent of a user's question.
    ---
    parameters:
      - name: question
        in: body
        type: string
        required: true
        description: The question whose intent needs to be classified
    responses:
      200:
        description: Successfully classified the intent of the question
        examples:
          application/json:
            {
              "category": "withdrawal_limit"
            }
      400:
        description: Bad request, missing question
        examples:
          application/json:
            {
              "error": "Question is required"
            }
      500:
        description: Internal server error
        examples:
          application/json:
            {
              "error": "Error classifying intent: <error details>"
            }
    """
    try:
        data = request.json
        question = data.get('question')
        if not question:
            return jsonify({'error': 'Question is required'}), 400

        category = intent_service.classify_question(question)
        return jsonify({'category': category})
    except Exception as e:
        raise IntentClassificationError(f"Error classifying intent: {str(e)}")