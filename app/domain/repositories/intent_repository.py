from abc import ABC, abstractmethod
from typing import List, Dict
from domain.models.intent_model import IntentInput, IntentOutput

class IntentRepository(ABC):
    @abstractmethod
    def save_intents(self, intents: List[IntentOutput]) -> None:
        pass