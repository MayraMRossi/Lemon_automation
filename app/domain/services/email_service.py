from typing import List
from domain.models.email_model import EmailInput, EmailOutput
from domain.repositories.email_repository import EmailRepository
from infrastructure.nlp.llm_classifier import LlmClassifier
from infrastructure.nlp.summarizer import Summarizer


class EmailService:
    def __init__(self, repository: EmailRepository, classifier: LlmClassifier, summarizer: Summarizer):
        self.repository = repository
        self.classifier = classifier
        self.summarizer = summarizer

    def process_emails(self, emails: List[EmailInput]) -> List[EmailOutput]:
        categories = {
            "Consultas de Crypto": "Consultas relacionadas con criptomonedas y su uso.",
            "Consultas de Banking": "Consultas relacionadas con servicios bancarios.",
            "Consultas de Tarjeta": "Consultas relacionadas con tarjetas de crédito y débito.",
            "Otro": "Cualquier otra consulta que no encaje en las categorías anteriores."
        }
        # TODO: Llevar esto a uan constante
        results = []
        for email in emails:
            category = self.classifier.classify(email.body, categories)
            summary = self.summarizer.summarize(email.body)
            cvu = self.extract_cvu(email.body) if category == "Consultas de Banking" else None

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

    def extract_cvu(self, body: str) -> str:
        import re
        match = re.search(r"\b\d{22}\b", body)
        return match.group(0) if match else None