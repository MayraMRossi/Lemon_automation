from typing import List
from domain.repositories.intent_repository import IntentRepository
from domain.models.intent_model import IntentOutput
from infrastructure.persistence.db_connection import SessionLocal

class SQLAlchemyIntentRepository(IntentRepository):
    def __init__(self):
        self.db = SessionLocal()

    def save_intents(self, intents: List[IntentOutput]) -> None:
        for intent in intents:
            self.db.add(intent)
        self.db.commit()