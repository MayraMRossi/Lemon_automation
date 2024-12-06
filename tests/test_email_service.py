import unittest
from unittest.mock import patch, MagicMock
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from domain.services.email_service import EmailService
from domain.models.email_model import EmailInput, EmailOutput
from infrastructure.nlp.llm_classifier import LlmClassifier
from infrastructure.nlp.summarizer import Summarizer
from utils.exceptions import EmailProcessingError

class TestEmailService(unittest.TestCase):
    def setUp(self):
        self.classifier_mock = MagicMock(spec=LlmClassifier)
        self.summarizer_mock = MagicMock(spec=Summarizer)
        self.repository_mock = MagicMock()
        self.service = EmailService(
            repository=self.repository_mock,
            classifier=self.classifier_mock,
            summarizer=self.summarizer_mock
        )

    def test_process_emails(self):
        print("Testing process_emails method...")
        emails = [
            EmailInput(customer_id=1, subject="Test", body="This is a test email about banking"),
            EmailInput(customer_id=2, subject="Test", body="This is a test email about crypto")
        ]
        self.classifier_mock.classify.side_effect = ["Banking Queries", "Crypto Queries"]
        self.summarizer_mock.summarize.side_effect = ["Summary 1", "Summary 2"]

        results = self.service.process_emails(emails)

        self.assertEqual(len(results), 2)
        self.assertEqual(results[0].category, "Banking Queries")
        self.assertEqual(results[1].category, "Crypto Queries")
        print("process_emails method test passed.")

    def test_process_emails_with_error(self):
        print("Testing process_emails method with error...")
        emails = [
            EmailInput(customer_id=1, subject="Test", body="This is a test email about banking")
        ]
        self.classifier_mock.classify.side_effect = Exception("Classification error")

        with self.assertRaises(EmailProcessingError):
            self.service.process_emails(emails)
        print("process_emails method with error test passed.")

if __name__ == "__main__":
    unittest.main()