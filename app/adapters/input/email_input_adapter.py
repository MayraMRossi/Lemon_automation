import pandas as pd
from typing import List
from domain.models.email_model import EmailInput

class EmailInputAdapter:
    def read_emails(self, file_path: str) -> List[EmailInput]:
        df = pd.read_csv(file_path, quotechar='"', quoting=1)
        print(df)
        return [EmailInput(**row) for row in df.to_dict(orient="records")]