import pandas as pd
from typing import List
from domain.models.intent_model import IntentOutput

class IntentOutputAdapter:
    def save_intents(self, intents: List[IntentOutput], file_path: str) -> None:
        df = pd.DataFrame([intent.dict() for intent in intents])
        df.to_csv(file_path, index=False)