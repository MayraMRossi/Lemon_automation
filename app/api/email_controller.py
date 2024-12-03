from flask import Blueprint, request, jsonify
from domain.services.email_service import EmailService
from adapters.input.email_input_adapter import EmailInputAdapter
from adapters.output.email_output_adapter import EmailOutputAdapter
from infrastructure.persistence.email_repository_impl import SQLAlchemyEmailRepository
from infrastructure.nlp.classifier import Classifier
from infrastructure.nlp.summarizer import Summarizer

email_blueprint = Blueprint("email", __name__)
email_service = EmailService(
    repository=SQLAlchemyEmailRepository(),
    classifier=Classifier(),
    summarizer=Summarizer()
)

@email_blueprint.route("/process", methods=["POST"])
def process_emails():
    try:
        input_adapter = EmailInputAdapter()
        output_adapter = EmailOutputAdapter()
        emails = input_adapter.read_emails("data/emails.csv")
        processed_emails = email_service.process_emails(emails)
        output_adapter.save_emails(processed_emails, "data/processed_emails.csv")
        return jsonify({"message": "Emails processed successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500