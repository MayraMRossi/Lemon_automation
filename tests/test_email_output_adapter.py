import unittest
from unittest.mock import patch
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from adapters.output.email_output_adapter import EmailOutputAdapter
from domain.models.email_model import EmailOutput
from utils.exceptions import FileWriteError

class TestEmailOutputAdapter(unittest.TestCase):
    @patch('pandas.DataFrame.to_csv')
    def test_save_emails(self, mock_to_csv):
        print("Testing save_emails method...")
        emails = [
            EmailOutput(customer_id=1, subject="Test 1", category="Category 1", summary="Summary 1"),
            EmailOutput(customer_id=2, subject="Test 2", category="Category 2", summary="Summary 2")
        ]

        adapter = EmailOutputAdapter()
        adapter.save_emails(emails)

        mock_to_csv.assert_called_once()
        print("save_emails method test passed.")

    @patch('pandas.DataFrame.to_csv')
    def test_save_emails_with_error(self, mock_to_csv):
        print("Testing save_emails method with error...")
        mock_to_csv.side_effect = Exception("File write error")

        emails = [
            EmailOutput(customer_id=1, subject="Test 1", category="Category 1", summary="Summary 1")
        ]

        adapter = EmailOutputAdapter()
        with self.assertRaises(FileWriteError):
            adapter.save_emails(emails)
        print("save_emails method with error test passed.")

if __name__ == "__main__":
    unittest.main()