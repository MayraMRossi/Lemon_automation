from abc import ABC, abstractmethod
from typing import List
from domain.models.rag_model import RAGQueryOutput

class RAGRepository(ABC):
    @abstractmethod
    def save_queries(self, queries: List[RAGQueryOutput]) -> None:
        pass