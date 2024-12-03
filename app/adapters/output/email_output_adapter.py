import pandas as pd
from typing import List
from domain.models.email_model import EmailOutput

class EmailOutputAdapter:
    def save_emails(self, emails: List[EmailOutput], file_path: str) -> None:
        df = pd.DataFrame([email.dict() for email in emails])
        df.to_csv(file_path, index=False)