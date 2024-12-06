SUMMARIZATION_PROMPT = """
Resume el siguiente mensaje de manera concisa, asegurándote de que el resumen no tenga más de 150 palabras.
Enfócate en capturar los puntos clave, omitiendo detalles innecesarios.

Mensaje: "{message}"

Tu respuesta debe contener solo la versión resumida del mensaje en español, estrictamente dentro del límite de 150 palabras. No agregues texto adicional, explicaciones ni saludos.
"""

CLASSIFICATION_PROMPT = """
Clasifica el siguiente mensaje en una de estas categorías:
{category_descriptions}
Si el mensaje no coincide con ninguna categoría, responde solo con "Otro".
Mensaje: "{message}"
Responde únicamente con el nombre de la categoría:
"""

RESPONSE_GENERATION_PROMPT = """
Responde a la siguiente consulta basada en el contexto proporcionado:
Consulta: "{query}"
Contexto: "{context}"
Tu respuesta debe ser concisa y relevante para la consulta, no añadas información extra, por favor sé amable y usa emojis.
"""