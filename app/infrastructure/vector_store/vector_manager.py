from llama_index import VectorStoreIndex, Document

class VectorManager:
    def __init__(self):
        self.index = None

    def build_index(self, documents):
        self.index = VectorStoreIndex(documents)

    def search_vectors(self, query, top_k=5):
        response = self.index.query(query, response_mode="compact", similarity_top_k=top_k)
        return {"response": response.response, "context": response.source_nodes}