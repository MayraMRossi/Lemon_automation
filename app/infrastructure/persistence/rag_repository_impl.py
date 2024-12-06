from typing import List
from domain.repositories.rag_repository import RAGRepository
from domain.models.rag_model import RAGQueryOutput
from infrastructure.persistence.db_connection import SessionLocal
from utils.exceptions import DatabaseConnectionError

class SQLAlchemyRAGRepository(RAGRepository):
    """Repository implementation for saving RAG queries using SQLAlchemy."""

    def __init__(self):
        try:
            self.db = SessionLocal()
        except Exception as e:
            raise DatabaseConnectionError(f"Error initializing database session: {str(e)}")

    def save_queries(self, queries: List[RAGQueryOutput]) -> None:
        """
        Saves a list of RAGQueryOutput models to the database.

        Args:
            queries (List[RAGQueryOutput]): A list of RAGQueryOutput models.
        """
        try:
            for query in queries:
                self.db.add(query)
            self.db.commit()
        except Exception as e:
            raise DatabaseConnectionError(f"Error saving RAG queries to database: {str(e)}")