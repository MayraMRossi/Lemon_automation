from abc import ABC, abstractmethod
from typing import List, Dict
from domain.models.rag_model import RAGQueryInput, RAGQueryOutput

class RAGRepository(ABC):
    @abstractmethod
    def save_queries(self, queries: List[RAGQueryOutput]) -> None:
        pass