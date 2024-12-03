from abc import ABC, abstractmethod
from typing import List, Dict
from domain.models.email_model import EmailInput, EmailOutput

class EmailRepository(ABC):
    @abstractmethod
    def save_emails(self, emails: List[EmailOutput]) -> None:
        pass