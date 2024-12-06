import pandas as pd
from typing import List
from domain.models.email_model import EmailInput
from utils.constants import EMAILS_CSV_PATH
from utils.exceptions import FileReadError

class EmailInputAdapter:
    """Adapter to read emails from a CSV file and convert them into EmailInput models."""

    def read_emails(self) -> List[EmailInput]:
        """
        Reads emails from a CSV file and converts them into a list of EmailInput models.

        Returns:
            List[EmailInput]: A list of EmailInput models.
        """
        try:
            df = pd.read_csv(EMAILS_CSV_PATH, quotechar='"', quoting=1)
            return [EmailInput(**row) for row in df.to_dict(orient="records")]
        except Exception as e:
            raise FileReadError(f"Error reading emails from CSV: {str(e)}")