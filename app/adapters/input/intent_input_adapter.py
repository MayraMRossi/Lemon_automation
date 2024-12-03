import pandas as pd
from typing import List
from domain.models.intent_model import IntentInput

class IntentInputAdapter:
    def read_intents(self, file_path: str) -> List[IntentInput]:
        df = pd.read_csv(file_path)
        return [IntentInput(**row) for row in df.to_dict(orient="records")]