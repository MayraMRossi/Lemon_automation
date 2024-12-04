from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


class Classifier:
    categories = {
        "Consultas de Crypto": "Consultas relacionadas con criptomonedas y su uso.",
        "Consultas de Banking": "Consultas relacionadas con servicios bancarios.",
        "Consultas de Tarjeta": "Consultas relacionadas con tarjetas de crédito y débito.",
        "Otro": "Cualquier otra consulta que no encaje en las categorías anteriores."
    }

    def classify(self, message: str) -> str:
        category_descriptions = "\n".join([f'"{category}": {desc}' for category, desc in self.categories.items()])

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
                temperature=0
            )
            rag_chain = prompt | llm | StrOutputParser()
            answer = rag_chain.invoke({"message": message})
            return answer.replace('"', "")
        except Exception as e:
            print(f"Error: {e}")
            return f"Error: {e}"