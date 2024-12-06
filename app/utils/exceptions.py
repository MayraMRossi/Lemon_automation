# exceptions.py

class EmailProcessingError(Exception):
    """Exception raised for errors during email processing."""
    pass

class IntentClassificationError(Exception):
    """Exception raised for errors during intent classification."""
    pass

class RAGQueryError(Exception):
    """Exception raised for errors during RAG query processing."""
    pass

class DatabaseConnectionError(Exception):
    """Exception raised for errors during database connection."""
    pass

class FileReadError(Exception):
    """Exception raised for errors during file reading."""
    pass

class FileWriteError(Exception):
    """Exception raised for errors during file writing."""
    pass

class ModelLoadingError(Exception):
    """Exception raised for errors during model loading."""
    pass

class VectorStoreError(Exception):
    """Exception raised for errors during vector store operations."""
    pass

class LLMIntegrationError(Exception):
    """Exception raised for errors during LLM integration."""
    pass

class SummarizationError(Exception):
    """Exception raised for errors during summarization."""
    pass

class ClassificationError(Exception):
    """Exception raised for errors during classification."""
    pass