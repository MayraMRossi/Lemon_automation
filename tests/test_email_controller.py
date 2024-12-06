import unittest
from unittest.mock import patch
from flask import Flask
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from api.email_controller import email_blueprint, process_emails
from utils.exceptions import EmailProcessingError

class TestEmailController(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(email_blueprint)
        self.client = self.app.test_client()

    @patch('api.email_controller.EmailInputAdapter')
    @patch('api.email_controller.EmailOutputAdapter')
    @patch('api.email_controller.EmailService')
    def test_process_emails(self, mock_email_service, mock_output_adapter, mock_input_adapter):
        print("Testing process_emails endpoint...")
        mock_input_adapter_instance = mock_input_adapter.return_value
        mock_input_adapter_instance.read_emails.return_value = []
        mock_email_service_instance = mock_email_service.return_value
        mock_email_service_instance.process_emails.return_value = []
        mock_output_adapter_instance = mock_output_adapter.return_value

        response = self.client.post('/emails/process')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Emails processed successfully"})
        print("process_emails endpoint test passed.")

    @patch('api.email_controller.EmailInputAdapter')
    @patch('api.email_controller.EmailOutputAdapter')
    @patch('api.email_controller.EmailService')
    def test_process_emails_with_error(self, mock_email_service, mock_output_adapter, mock_input_adapter):
        print("Testing process_emails endpoint with error...")
        mock_input_adapter_instance = mock_input_adapter.return_value
        mock_input_adapter_instance.read_emails.return_value = []
        mock_email_service_instance = mock_email_service.return_value
        mock_email_service_instance.process_emails.side_effect = EmailProcessingError("Processing error")

        response = self.client.post('/emails/process')

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {"error": "Error processing emails: Processing error"})
        print("process_emails endpoint with error test passed.")

if __name__ == "__main__":
    unittest.main()