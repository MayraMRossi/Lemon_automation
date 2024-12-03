from flask import Blueprint, request, jsonify
from domain.services.intent_service import IntentService
from adapters.input.intent_input_adapter import IntentInputAdapter
from adapters.output.intent_output_adapter import IntentOutputAdapter
from infrastructure.persistence.intent_repository_impl import SQLAlchemyIntentRepository
from infrastructure.nlp.classifier import Classifier

intent_blueprint = Blueprint("intent", __name__)
intent_service = IntentService(
    repository=SQLAlchemyIntentRepository(),
    classifier=Classifier()
)

@intent_blueprint.route("/classify", methods=["POST"])
def classify_intent():
    try:
        input_adapter = IntentInputAdapter()
        output_adapter = IntentOutputAdapter()
        intents = input_adapter.read_intents("data/intents.csv")
        classified_intents = [intent_service.classify_intent(intent) for intent in intents]
        output_adapter.save_intents(classified_intents, "data/classified_intents.csv")
        return jsonify({"message": "Intents classified successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500