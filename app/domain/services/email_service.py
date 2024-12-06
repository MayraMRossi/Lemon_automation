from typing import List
from domain.models.email_model import EmailInput, EmailOutput
from domain.repositories.email_repository import EmailRepository
from infrastructure.nlp.llm_classifier import LlmClassifier
from infrastructure.nlp.summarizer import Summarizer
from utils.constants import EMAIL_CATEGORIES
from utils.exceptions import EmailProcessingError


class EmailService:
    """Service to process emails by classifying and summarizing their content."""

    def __init__(self, repository: EmailRepository, classifier: LlmClassifier, summarizer: Summarizer):
        self.repository = repository
        self.classifier = classifier
        self.summarizer = summarizer

    def process_emails(self, emails: List[EmailInput]) -> List[EmailOutput]:
        """
        Processes a list of emails by classifying and summarizing their content.

        Args:
            emails (List[EmailInput]): A list of EmailInput models.

        Returns:
            List[EmailOutput]: A list of processed EmailOutput models.
        """
        try:
            results = []
            for email in emails:
                category = self.classifier.classify(email.body, EMAIL_CATEGORIES)
                summary = self.summarizer.summarize(email.body)
                cvu = self.extract_cvu(email.body) if category == "Banking Queries" else None

                results.append(
                    EmailOutput(
                        customer_id=email.customer_id,
                        subject=email.subject,
                        category=category,
                        summary=summary,
                        cvu=cvu
                    )
                )
            return results
        except Exception as e:
            raise EmailProcessingError(f"Error processing emails: {str(e)}")

    def extract_cvu(self, body: str) -> str:
        """
        Extracts a CVU (Customer Verification Unit) from the email body.

        Args:
            body (str): The body of the email.

        Returns:
            str: The extracted CVU.
        """
        import re
