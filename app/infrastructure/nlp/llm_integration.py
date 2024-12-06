from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from utils.exceptions import LLMIntegrationError
from utils.prompts import RESPONSE_GENERATION_PROMPT

class LLMIntegration:
    """Integration with a language model to generate responses based on provided context."""

    def generate_response(self, query: str, context: str) -> str:
        """
        Generates a response to the given query based on the provided context.

        Args:
            query (str): The query text.
            context (str): The context text.

        Returns:
            str: The generated response.
        """
        try:
            prompt = PromptTemplate(
                template=RESPONSE_GENERATION_PROMPT,
                input_variables=["query", "context"]
            )

            llm = ChatOllama(
                model="llama3.2",
                temperature=0,
                max_tokens=200
            )
            rag_chain = prompt | llm | StrOutputParser()
            answer = rag_chain.invoke({"query": query, "context": context})
            return answer.replace('"', "")
        except Exception as e:
            raise LLMIntegrationError(f"Error generating response: {str(e)}")