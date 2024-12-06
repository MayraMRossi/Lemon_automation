from typing import List
from domain.repositories.intent_repository import IntentRepository
from domain.models.intent_model import IntentOutput
from infrastructure.persistence.db_connection import SessionLocal
from utils.exceptions import DatabaseConnectionError

class SQLAlchemyIntentRepository(IntentRepository):
    """Repository implementation for saving intents using SQLAlchemy."""

    def __init__(self):
        try:
            self.db = SessionLocal()
        except Exception as e:
            raise DatabaseConnectionError(f"Error initializing database session: {str(e)}")

    def save_intents(self, intents: List[IntentOutput]) -> None:
        """
        Saves a list of IntentOutput models to the database.

        Args:
            intents (List[IntentOutput]): A list of IntentOutput models.
        """
        try:
            for intent in intents:
                self.db.add(intent)
            self.db.commit()
        except Exception as e:
            raise DatabaseConnectionError(f"Error saving intents to database: {str(e)}")