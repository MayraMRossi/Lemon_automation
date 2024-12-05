from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


class Summarizer:
    def summarize(self, message: str) -> str:
        print("Summarizing")
        prompt = PromptTemplate(
            template=f"""
            Summarize the following message in a concise manner, ensuring the summary is no longer than 150 words.
            Focus on capturing the key points, omitting unnecessary details.

            Message: "{message}"

            Your response should contain only the summarized version of the message, strictly within the 150-word limit. Do not add any extra text, explanations, or greetings.
            """,
            input_variables=["message"]
        )

        try:
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
            print(f"Error: {e}")
            return f"Error: {e}"

        # TODO: revisar los fallos

