import json
from domain.models.rag_model import RAGQueryOutput

class RAGOutputAdapter:
    def save_queries(self, queries: List[RAGQueryOutput], file_path: str) -> None:
        with open(file_path, 'w') as file:
            json.dump([query.dict() for query in queries], file, indent=4)