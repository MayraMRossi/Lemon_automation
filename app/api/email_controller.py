from flask import Blueprint, jsonify
from domain.services.email_service import EmailService
from adapters.input.email_input_adapter import EmailInputAdapter
from adapters.output.email_output_adapter import EmailOutputAdapter
from infrastructure.persistence.email_repository_impl import SQLAlchemyEmailRepository
from infrastructure.nlp.llm_classifier import LlmClassifier
from infrastructure.nlp.summarizer import Summarizer
from utils.exceptions import EmailProcessingError

email_blueprint = Blueprint("email", __name__)
email_service = EmailService(
    repository=SQLAlchemyEmailRepository(),
    classifier=LlmClassifier(),
    summarizer=Summarizer()
)

@email_blueprint.route("/process", methods=["POST"])
def process_emails():
    """
    Endpoint to process emails. Reads emails from a CSV, processes them, and saves the results.
    ---
    parameters:
      - name: email_file
        in: formData
        type: file
        required: true
        description: CSV file containing email data to be processed
    responses:
      200:
        description: Emails processed successfully
        examples:
          application/json: {"message": "Emails processed successfully"}
      400:
        description: Bad request, possibly due to an invalid file or missing parameter
        examples:
          application/json: {"message": "Error processing emails"}
      500:
        description: Internal server error
        examples:
          application/json: {"message": "Error processing emails: <error details>"}
    """
    try:
        input_adapter = EmailInputAdapter()
        output_adapter = EmailOutputAdapter()
        emails = input_adapter.read_emails()
        processed_emails = email_service.process_emails(emails)
        output_adapter.save_emails(processed_emails)
        return jsonify({"message": "Emails processed successfully"})
    except Exception as e:
        raise EmailProcessingError(f"Error processing emails: {str(e)}")