from flask import Blueprint, request, jsonify
from domain.services.intent_service import IntentService


intent_blueprint = Blueprint("intent", __name__)
intent_service = IntentService()

@intent_blueprint.route("/classify", methods=["POST"])
def classify_intent():
    try:
        data = request.json
        question = data.get('question')
        if not question:
            return jsonify({'error': 'Question is required'}), 400

        intent_service = IntentService()
        category = intent_service.classify_question(question)
        return jsonify({'category': category})
    except Exception as e:
        return jsonify({"error": str(e)}), 500