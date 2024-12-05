from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


class LlmClassifier:

    def classify(self, message: str, categories: dict) -> str:
        category_descriptions = "\n".join([f'"{category}": {desc}' for category, desc in categories.items()])

        prompt = PromptTemplate(
            template=f"""
            Classify the following message into one of these categories:
            {category_descriptions}
            If the message does not match any category, respond only with "Other".
            Message: "{message}"
            Respond only with the category name:
            """,
            input_variables=["message"]
        )

        try:
            llm = ChatOllama(
                model="llama3.2",
                temperature=0,
                max_tokens=200
            )
            rag_chain = prompt | llm | StrOutputParser()
            answer = rag_chain.invoke({"message": message})
            return answer.replace('"', "")
        except Exception as e:
            print(f"Error: {e}")
            return f"Error: {e}"

        # TODO: revisar que si es error no lo agregue al archivo