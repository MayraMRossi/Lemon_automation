from typing import List
from domain.repositories.email_repository import EmailRepository
from domain.models.email_model import EmailOutput
from infrastructure.persistence.db_connection import SessionLocal

class SQLAlchemyEmailRepository(EmailRepository):
    def __init__(self):
        self.db = SessionLocal()

    def save_emails(self, emails: List[EmailOutput]) -> None:
        for email in emails:
            self.db.add(email)
        self.db.commit()