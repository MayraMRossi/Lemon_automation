import unittest
from app.domain.services.email_service import EmailService
from app.domain.models.email_model import EmailInput, EmailOutput
from app.infrastructure.nlp.classifier import Classifier
from app.infrastructure.nlp.summarizer import Summarizer

class TestEmailService(unittest.TestCase):
    def setUp(self):
        self.service = EmailService(
            repository=MockEmailRepository(),
            classifier=Classifier(),
            summarizer=Summarizer()
        )

    def test_process_emails(self):
        emails = [
            EmailInput(customer_id=1, subject="Test", body="This is a test email about banking"),
            EmailInput(customer_id=2, subject="Test", body="This is a test email about crypto")
        ]
        results = self.service.process_emails(emails)
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0].category, "Banking")
        self.assertEqual(results[1].category, "Crypto")

class MockEmailRepository:
    def save_emails(self, emails):
        pass

if __name__ == "__main__":
    unittest.main()