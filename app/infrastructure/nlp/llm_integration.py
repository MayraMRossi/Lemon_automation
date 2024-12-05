from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

class LLMIntegration:
    def generate_response(self, query: str, context: str) -> str:
        prompt = PromptTemplate(
            template=f"""
            Answer the following query based on the provided context:
            Query: "{query}"
            Context: "{context}"
            Your response should be concise and relevant to the query, please be kind and use emojis.
            """,
            input_variables=["query", "context"]
        )

        try:
            llm = ChatOllama(
                model="llama3.2",
                temperature=0,
                max_tokens=200
            )
            rag_chain = prompt | llm | StrOutputParser()
            answer = rag_chain.invoke({"query": query, "context": context})
            return answer.replace('"', "")
        except Exception as e:
            print(f"Error: {e}")
            return f"Error: {e}"