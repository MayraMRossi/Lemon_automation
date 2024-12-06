import unittest
from unittest.mock import patch
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from adapters.input.email_input_adapter import EmailInputAdapter
from domain.models.email_model import EmailInput
from utils.exceptions import FileReadError

class TestEmailInputAdapter(unittest.TestCase):
    @patch('pandas.read_csv')
    def test_read_emails(self, mock_read_csv):
        print("Testing read_emails method...")
        mock_df = pd.DataFrame({
            'customer_id': [1, 2],
            'subject': ['Test 1', 'Test 2'],
            'body': ['Body 1', 'Body 2']
        })
        mock_read_csv.return_value = mock_df

        adapter = EmailInputAdapter()
        emails = adapter.read_emails()

        self.assertEqual(len(emails), 2)
        self.assertIsInstance(emails[0], EmailInput)
        print("read_emails method test passed.")

    @patch('pandas.read_csv')
    def test_read_emails_with_error(self, mock_read_csv):
        print("Testing read_emails method with error...")
        mock_read_csv.side_effect = Exception("File read error")

        adapter = EmailInputAdapter()
        with self.assertRaises(FileReadError):
            adapter.read_emails()
        print("read_emails method with error test passed.")

if __name__ == "__main__":
    unittest.main()