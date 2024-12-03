from domain.repositories.rag_repository import RAGRepository
from domain.models.rag_model import RAGQueryOutput
from infrastructure.persistence.db_connection import SessionLocal

class SQLAlchemyRAGRepository(RAGRepository):
    def __init__(self):
        self.db = SessionLocal()

    def save_queries(self, queries: List[RAGQueryOutput]) -> None:
        for query in queries:
            self.db.add(query)
        self.db.commit()