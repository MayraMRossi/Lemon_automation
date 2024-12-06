from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from utils.exceptions import SummarizationError
from utils.prompts import SUMMARIZATION_PROMPT

class Summarizer:
    """Summarizes messages using a language model."""

    def summarize(self, message: str) -> str:
        """
        Summarizes the given message in a concise manner.

        Args:
            message (str): The message to summarize.

        Returns:
            str: The summarized message.
        """
        try:
            prompt = PromptTemplate(
                template=SUMMARIZATION_PROMPT,
                input_variables=["message"]
            )

            llm = ChatOllama(
                model="llama3.2",
                temperature=0
            )
            times = 3
            length = 151
            while times != 0 and length > 150:
                rag_chain = prompt | llm | StrOutputParser()
                answer = rag_chain.invoke({"message": message})
                length = len(answer.split())
                print(length)
                times -= 1
            if length <= 150:
                return answer.replace('"', "")
            return "Error: The summary exceeded the 150-character limit after multiple attempts."
        except Exception as e:
            raise SummarizationError(f"Error summarizing message: {str(e)}")