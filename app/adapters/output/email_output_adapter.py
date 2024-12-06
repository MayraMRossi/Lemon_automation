import pandas as pd
from typing import List
from domain.models.email_model import EmailOutput
from utils.constants import PROCESSED_EMAILS_CSV_PATH
from utils.exceptions import FileWriteError

class EmailOutputAdapter:
    """Adapter to save processed emails to a CSV file."""

    def save_emails(self, emails: List[EmailOutput]) -> None:
        """
        Saves a list of EmailOutput models to a CSV file.

        Args:
            emails (List[EmailOutput]): A list of EmailOutput models.
        """
        try:
            df = pd.DataFrame([email.dict() for email in emails])
            df.to_csv(PROCESSED_EMAILS_CSV_PATH, index=False)
        except Exception as e:
            raise FileWriteError(f"Error writing emails to CSV: {str(e)}")