from typing import List
import sys
import os
from domain.repositories.email_repository import EmailRepository
from domain.models.email_model import EmailOutput
from infrastructure.persistence.db_connection import SessionLocal
from utils.exceptions import DatabaseConnectionError

class SQLAlchemyEmailRepository(EmailRepository):
    """Repository implementation for saving emails using SQLAlchemy."""

    def __init__(self):
        try:
            self.db = SessionLocal()
        except Exception as e:
            raise DatabaseConnectionError(f"Error initializing database session: {str(e)}")

    def save_emails(self, emails: List[EmailOutput]) -> None:
        """
        Saves a list of EmailOutput models to the database.

        Args:
            emails (List[EmailOutput]): A list of EmailOutput models.
        """
        try:
            for email in emails:
                self.db.add(email)
            self.db.commit()
        except Exception as e:
            raise DatabaseConnectionError(f"Error saving emails to database: {str(e)}")