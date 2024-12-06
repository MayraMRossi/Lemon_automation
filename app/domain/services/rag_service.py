from infrastructure.vector_store.chroma_vector_store import ChromaVectorStore
from infrastructure.nlp.llm_integration import LLMIntegration
from domain.models.rag_model import RAGQueryOutput
from sklearn.feature_extraction.text import TfidfVectorizer
from utils.constants import VECTOR_STORE_PATH, VECTOR_STORE_COLLECTION_NAME, QUERY_TOP_K
from utils.exceptions import RAGQueryError, VectorStoreError

class RAGService:
    """Service to perform Retrieval-Augmented Generation (RAG) queries."""

    def __init__(self):
        try:
            self.vector_store = ChromaVectorStore(collection_name=VECTOR_STORE_COLLECTION_NAME, path=VECTOR_STORE_PATH)
            self.llm = LLMIntegration()
            self.vectorizer = TfidfVectorizer()
        except Exception as e:
            raise VectorStoreError(f"Error initializing vector store: {str(e)}")

    def add_document_to_vector_store(self, document: str, context: str, url: str):
        """
        Adds a single document to the vector store with metadata (context and URL).

        Args:
            document (str): The document text.
            context (str): The context of the document.
            url (str): The URL associated with the document.
        """
        try:
            document_list = [document]
            metadata_list = [{"context": context, "url": url}]
            self.vector_store.add_documents(documents=document_list, metadatas=metadata_list)
            print(f"Document added: {document}")
        except Exception as e:
            raise VectorStoreError(f"Error adding document to vector store: {str(e)}")

    def query_rag(self, query: str) -> dict:
        """
        Performs a retrieval-augmented generation (RAG) query.

        Args:
            query (str): The text of the query to search.

        Returns:
            dict: A dictionary with the generated response, context, and associated URLs.
        """
        try:
            document_count = self.vector_store.check_documents_count()
            if document_count == 0:
                print("No documents in the collection.")
                return {"answer": "Sorry, no relevant information was found.", "context": "", "urls": []}

            query_result = self.vector_store.query(query_text=query, top_k=QUERY_TOP_K)
            print(f"Query result: {query_result}")

            if not query_result:
                print("No relevant documents found in the query result.")
                return {"answer": "Sorry, no relevant information was found.", "context": "", "urls": []}

            context = query_result.get('context', "No relevant context found.")
            urls = query_result.get('urls', [])

            response = self.llm.generate_response(query=query, context=context)

            return RAGQueryOutput(answer=response, context=context, urls=urls).model_dump()
        except Exception as e:
            raise RAGQueryError(f"Error querying RAG service: {str(e)}")