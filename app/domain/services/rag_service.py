from infrastructure.vector_store.chroma_vector_store import ChromaVectorStore
from infrastructure.nlp.llm_integration import LLMIntegration
from domain.models.rag_model import RAGQueryOutput
from sklearn.feature_extraction.text import TfidfVectorizer
import os
import sys

class RAGService:
    def __init__(self):
        # Initialize the vector store and the language model (LLM) integration
        absolute_path = os.path.abspath("app/data/vector_store")
        print(f"Ruta absoluta: {absolute_path}")
        self.vector_store = ChromaVectorStore(collection_name='help_center', path=absolute_path)
        self.llm = LLMIntegration()  # Assuming LLMIntegration is set up correctly
        self.vectorizer = TfidfVectorizer()

    def add_document_to_vector_store(self, document: str, context: str, url: str):
        """
        Adds a single document to the vector store with metadata (context and URL).
        Ensures that the documents and metadata are passed as lists.
        """
        try:
            # Convert the document and metadata into lists
            document_list = [document]  # Convert the document into a list
            metadata_list = [{"context": context, "url": url}]  # Convert the metadata into a list

            # Add the document and metadata to the vector store
            self.vector_store.add_documents(documents=document_list, metadatas=metadata_list)
            print(f"Document added: {document}")
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)  # Exit with an error code

    def query_rag(self, query: str) -> dict:
        """
        Performs a retrieval-augmented generation (RAG) query.
        Retrieves relevant documents from the vector store and generates a response
        using the LLM based on the retrieved context.

        :param query: The text of the query to search.
        :return: A dictionary with the generated response, context, and associated URLs.
        """

        try:
            # Check if there are any documents in the vector store
            document_count = self.vector_store.check_documents_count()
            if document_count == 0:
                print("No documents in the collection.")
                return {"answer": "Sorry, no relevant information was found.", "context": "", "urls": []}

            # Perform the query in the collection to retrieve relevant documents
            query_result = self.vector_store.query(query_text=query, top_k=5)
            print(f"Query result: {query_result}")  # Debug line

            if not query_result:
                print("No relevant documents found in the query result.")
                return {"answer": "Sorry, no relevant information was found.", "context": "", "urls": []}

            # Extract context and URLs from the query result
            context = query_result.get('context', "No relevant context found.")
            urls = query_result.get('urls', [])

            # Generate a response using the LLM based on the retrieved context
            response = self.llm.generate_response(query=query, context=context)

            # Return the response as an output model (including context and URLs)
            return RAGQueryOutput(answer=response, context=context, urls=urls).model_dump()
        except Exception as e:
            print(f"Error: {e}")
            return {"error": str(e)}  # Return error message instead of exiting
