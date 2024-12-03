import json
from domain.models.rag_model import RAGQueryInput

class RAGInputAdapter:
    def read_queries(self, file_path: str) -> List[RAGQueryInput]:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return [RAGQueryInput(**query) for query in data]