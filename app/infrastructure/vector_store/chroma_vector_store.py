from chromadb import PersistentClient
import uuid
from sentence_transformers import SentenceTransformer
from chromadb.errors import InvalidDimensionException
import sys

class ChromaVectorStore:
    def __init__(self, collection_name: str, path: str):
        """
        Constructor de la clase ChromaVectorStore.
        Maneja la inicialización del cliente y el modelo de embedding.
        """
        self.client = PersistentClient(path=path)
        self.collection = self.client.get_or_create_collection(name=collection_name)
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

    def add_documents(self, documents: list, metadatas: list):
        """
        Agrega documentos y sus metadatos al almacén de vectores.
        :param documents: Lista de documentos (textos).
        :param metadatas: Lista de metadatas asociados (debe incluir "url").
        """
        try:
            if len(documents) != len(metadatas):
                raise ValueError("Documents and metadata must have the same length.")

            ids = [str(uuid.uuid4()) for _ in documents]  # Genera IDs únicos

            # Generar embeddings
            vectors = self.embedding_model.encode(documents).tolist()

            # Verificar dimensión de embeddings si ya existen datos en la colección
            if self.collection.count() > 0:
                existing_embeddings = self.collection.get(include=["embeddings"])['embeddings']
                if len(existing_embeddings) > 0 and len(vectors[0]) != len(existing_embeddings[0]):
                    raise InvalidDimensionException(
                        f"Embedding dimension {len(vectors[0])} does not match collection dimensionality {len(existing_embeddings[0])}"
                    )

            # Agregar documentos a la colección
            self.collection.add(documents=documents, embeddings=vectors, metadatas=metadatas, ids=ids)
            print(f"Documents and vectors added with IDs: {ids}")
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

    def query(self, query_text: str, top_k: int = 5):
        """
        Realiza una consulta en la colección y devuelve los resultados más relevantes.
        :param query_text: Texto de consulta.
        :param top_k: Número de resultados relevantes a devolver.
        :return: Diccionario con los contextos y URLs relevantes.
        """
        try:
            all_documents = self.collection.get(include=["documents"])['documents']
            all_metadatas = self.collection.get(include=["metadatas"])['metadatas']

            if not all_documents:
                print("No documents found in the collection.")
                return {'context': "", 'urls': []}

            # Generar embedding de la consulta
            query_embedding = self.embedding_model.encode([query_text]).tolist()[0]

            # Realizar la consulta en la colección
            results = self.collection.query(query_embeddings=[query_embedding], n_results=top_k)

            # Extraer documentos y URLs relevantes
            relevant_documents = results['documents'][0]
            relevant_metadatas = results['metadatas'][0]

            context = "\n".join(relevant_documents)
            urls = [metadata['url'] for metadata in relevant_metadatas]

            return {'context': context, 'urls': urls}
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

    def clear_collection(self):
        """
        Limpia todos los documentos de la colección.
        """
        try:
            self.collection.delete(where={"$exists": True})
            print("Collection cleared.")
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

    def check_documents_count(self):
        """
        Muestra la cantidad de documentos en la colección.
        """
        try:
            count = self.collection.count()
            print(f"Number of documents in the collection: {count}")
            return count
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)