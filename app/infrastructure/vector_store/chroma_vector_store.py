from chromadb import PersistentClient
import uuid
from sentence_transformers import SentenceTransformer
from chromadb.errors import InvalidDimensionException
import sys
from utils.exceptions import VectorStoreError

class ChromaVectorStore:
    """Vector store using ChromaDB."""

    def __init__(self, collection_name: str, path: str):
        """
        Constructor for the ChromaVectorStore class.

        Args:
            collection_name (str): The name of the collection.
            path (str): The path to the vector store.
        """
        try:
            self.client = PersistentClient(path=path)
            self.collection = self.client.get_or_create_collection(name=collection_name)
            self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        except Exception as e:
            raise VectorStoreError(f"Error initializing vector store: {str(e)}")

    def add_documents(self, documents: list, metadatas: list):
        """
        Adds documents and their metadata to the vector store.

        Args:
            documents (list): A list of document texts.
            metadatas (list): A list of metadata dictionaries.
        """
        try:
            if len(documents) != len(metadatas):
                raise ValueError("Documents and metadata must have the same length.")

            ids = [str(uuid.uuid4()) for _ in documents]
            vectors = self.embedding_model.encode(documents).tolist()

            if self.collection.count() > 0:
                existing_embeddings = self.collection.get(include=["embeddings"])['embeddings']
                if len(existing_embeddings) > 0 and len(vectors[0]) != len(existing_embeddings[0]):
                    raise InvalidDimensionException(
                        f"Embedding dimension {len(vectors[0])} does not match collection dimensionality {len(existing_embeddings[0])}"
                    )

            self.collection.add(documents=documents, embeddings=vectors, metadatas=metadatas, ids=ids)
            print(f"Documents and vectors added with IDs: {ids}")
        except Exception as e:
            raise VectorStoreError(f"Error adding documents to vector store: {str(e)}")

    def query(self, query_text: str, top_k: int = 5):
        """
        Performs a query in the collection and returns the most relevant results.

        Args:
            query_text (str): The text of the query.
            top_k (int): The number of results to return.

        Returns:
            dict: A dictionary with the relevant documents, context, and URLs.
        """
        try:
            all_documents = self.collection.get(include=["documents"])['documents']
            all_metadatas = self.collection.get(include=["metadatas"])['metadatas']

            if not all_documents:
                print("No documents found in the collection.")
                return {'context': "", 'urls': []}

            query_embedding = self.embedding_model.encode([query_text]).tolist()[0]
            results = self.collection.query(query_embeddings=[query_embedding], n_results=top_k)

            relevant_documents = results['documents'][0]
            relevant_metadatas = results['metadatas'][0]

            context = "\n".join(relevant_documents)
            urls = [metadata['url'] for metadata in relevant_metadatas]

            return {'context': context, 'urls': urls}
        except Exception as e:
            raise VectorStoreError(f"Error querying vector store: {str(e)}")

    def clear_collection(self):
        """
        Clears all documents from the collection.
        """
        try:
            self.collection.delete(where={"$exists": True})
            print("Collection cleared.")
        except Exception as e:
            raise VectorStoreError(f"Error clearing collection: {str(e)}")

    def check_documents_count(self):
        """
        Checks the number of documents in the collection.

        Returns:
            int: The number of documents in the collection.
        """
        try:
            count = self.collection.count()
            print(f"Number of documents in the collection: {count}")
            return count
        except Exception as e:
            raise VectorStoreError(f"Error checking documents count: {str(e)}")