from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from utils.exceptions import ClassificationError
from utils.prompts import CLASSIFICATION_PROMPT

class LlmClassifier:
    """Classifier that uses a language model to classify messages into predefined categories."""

    def classify(self, message: str, categories: dict) -> str:
        """
        Classifies the given message into one of the predefined categories.

        Args:
            message (str): The message to classify.
            categories (dict): A dictionary of categories and their descriptions.

        Returns:
            str: The classified category.
        """
        try:
            category_descriptions = "\n".join([f'"{category}": {desc}' for category, desc in categories.items()])

            prompt = PromptTemplate(
                template=f"""
                Clasifica el siguiente mensaje en una de estas categorías:
                {category_descriptions}
                Si el mensaje no coincide con ninguna categoría, responde solo con "Otro".
                Mensaje: "{message}"
                Responde únicamente con el nombre de la categoría:
                """,
                input_variables=["message"]
            )

            llm = ChatOllama(
                model="llama3.2",
                temperature=0,
                max_tokens=200
            )
            rag_chain = prompt | llm | StrOutputParser()
            answer = rag_chain.invoke({"message": message})
            return answer.replace('"', "")
        except Exception as e:
            raise ClassificationError(f"Error classifying message: {str(e)}")