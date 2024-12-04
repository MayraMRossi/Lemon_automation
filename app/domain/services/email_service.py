from typing import List
from domain.models.email_model import EmailInput, EmailOutput
from domain.repositories.email_repository import EmailRepository
from infrastructure.nlp.classifier import Classifier
from infrastructure.nlp.summarizer import Summarizer

class EmailService:
    def __init__(self, repository: EmailRepository, classifier: Classifier, summarizer: Summarizer):
        self.repository = repository
        self.classifier = classifier
        self.summarizer = summarizer

    def process_emails(self, emails: List[EmailInput]) -> List[EmailOutput]:
        results = []
        for email in emails:
            category = self.classifier.classify(email.body)
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