
# Lemon Automation

## Table of Contents

1. [Exercise 1: Task Automation](#exercise-1-task-automation)
2. [Exercise 2: AI Integration](#exercise-2-ai-integration)
3. [Exercise 3: Retrieval-Augmented Generation (RAG) System](#exercise-3-retrieval-augmented-generation-rag-system)
4. [Exercise 4: Get Response](#exercise-4-get-response)

---

## Exercise 1: Task Automation

### Overview

The Customer Experience and Operations team manages a large volume of customer emails daily. These emails are usually in a predictable format and contain inquiries about Lemon’s products. To optimize this process, a tool has been developed to automate email classification and summarization.

### Requirements

1. **Email File Reading**: The tool should read email files in `.csv` or `.json` format with the following fields:
   - Customer ID
   - Subject
   - Message Body

2. **Email Classification**: Emails should be categorized into the following categories:
   - Crypto Queries
   - Banking Queries
   - Card Queries
   - Other

3. **Output File**: The processed results should be saved in a file with the following columns:
   - Customer ID
   - Subject
   - Category
   - Summary
   - CVU (if applicable)

4. **Summary Generation**: Generate a brief summary (maximum 150 words) for each email using Natural Language Processing (NLP). For emails categorized as "Banking Queries," extract and display the CVU if present.

### Execution Steps

1. **Setup Prerequisites**:
   - Download and install **Ollama** from its official website.
   - Use the command `ollama pull llama3.2` to download the generative AI model.
   - Ensure the input email file is located at `app/data/emails.csv`.

2. **Run the Server**:
   Start the server using the command:
   ```bash
   python app/main.py
   ```

3. **Process Emails**:
   Send a POST request to the endpoint `http://127.0.0.1:8000/emails/process` without a request body. For example:
   ```bash
   curl -X POST http://127.0.0.1:8000/emails/process
   ```

4. **Result**:
   - The processed email file will be saved at `app/data/processed_emails.csv`.

### Notes

- The **llama3.2** model runs slower on local machines. Optimization will be addressed in future iterations.

---

## Exercise 2: AI Integration

### Overview

To improve the efficiency of the chatbot for frequently asked customer questions, an Intent Classification model has been developed. This model helps classify and respond to common inquiries effectively.

### Requirements

1. **Intent Classification**: Train the model to classify questions into the following categories:
   - Crypto Withdrawals
   - Unrecognized Transactions
   - Fiat Withdrawals
   - Lost Card Report
   - Lemon Earn

2. **Dataset**: Prepare and use a dataset of 100–200 categorized questions for training.

### Execution Steps

1. **Run the Server**:
   Start the server using:
   ```bash
   python app/main.py
   ```

2. **Classify Intent**:
   Use the POST method to send a query to `http://127.0.0.1:8000/intents/classify`. For example:
   ```json
   {
    "question": "¿Cual es el limite de retiro de bitcoins?"
    }
   ```
   Response example:
   ```json
   {
    "category": "Retiros Crypto"
   }
   ```

### Notes

- The model is saved in the `app/models` folder and can be retrained using the `train_model.py` script in the `scripts` folder.

---

## Exercise 3: Retrieval-Augmented Generation (RAG) System

### Overview

The RAG system enables the chatbot to answer questions about Lemon’s help center by combining vector-based information retrieval with a Language Learning Model (LLM).

### Requirements

1. **Vector Database**: Store help center information in a vector database for efficient retrieval.
2. **LLM Integration**: Use the LLM to generate answers based on the retrieved information.

### Execution Steps

1. **Setup Prerequisites**:
   - Download and install **Ollama**.
   - Use the command `ollama pull llama3.2` to download the model.
   - The first time use the script `scrape_and_populate_vector_store.py` to populate the vector database.

2. **Run the Server**:
   Start the server using:
   ```bash
   python app/main.py
   ```

3. **Query the RAG System**:
   Send a POST request to `http://127.0.0.1:8000/rag/query`. For example:
   ```json
   {
    "query": "¿la tarjeta de lemon es visa??"
    }
   ```
   Example response:
   ```json
   {
    "answer": "¡Hola! 😊\n\nLa respuesta a tu pregunta es: Sí, la tarjeta de Lemon es Visa. 📈👍",
    "context": "Es la tarjeta prepaga de Lemon y la podés usar en cualquier comercio o página web del mundo que esté dentro de la red VISA.\n\nLemon Card es el puente entre tus crypto y el mundo tradicional, acompañándote en todas tus compras diarias. Con tu tarjeta podés pagar en todos los comercios del mundo que estén dentro de la red VISA.\n\n¿Qué necesito para tener mi Lemon Card?\n\nPara pedir tu tarjeta, tenés que cumplir los siguientes requisitos:\n\nSer mayor de 18 años.\n\nTener un documento de identidad argentino.\n\nTener una cuenta creada y validada en Lemon.\n\n¿Cómo pido mi Lemon Card?\n\nPara conocer cómo podés hacer para solicitar tu Lemon Card, entrá en este artículo:\n\n¿Hay un costo de mantenimiento?\n\nLa tarjeta no tiene costos de envío ni de mantenimiento.\n\n¿Qué beneficios tiene?\n\nOtras tarjetas ofrecen millas o puntos por tus consumos, pero en Lemon te regalamosBitcoin con cada compra que hagas.\n\nTambién te permite acceder a muchos beneficios, como por ejemplo:\nEs la tarjeta prepaga de Lemon y la podés usar en cualquier comercio o página web del mundo que esté dentro de la red VISA.\n\nLemon Card es el puente entre tus crypto y el mundo tradicional, acompañándote en todas tus compras diarias. Con tu tarjeta podés pagar en todos los comercios del mundo que estén dentro de la red VISA.\n\n¿Qué necesito para tener mi Lemon Card?\n\nPara pedir tu tarjeta, tenés que cumplir los siguientes requisitos:\n\nSer mayor de 18 años.\n\nTener un documento de identidad argentino.\n\nTener una cuenta creada y validada en Lemon.\n\n¿Cómo pido mi Lemon Card?\n\nPara conocer cómo podés hacer para solicitar tu Lemon Card, entrá en este artículo:\n\n¿Hay un costo de mantenimiento?\n\nLa tarjeta no tiene costos de envío ni de mantenimiento.\n\n¿Qué beneficios tiene?\n\nOtras tarjetas ofrecen millas o puntos por tus consumos, pero en Lemon te regalamosBitcoin con cada compra que hagas.\n\nTambién te permite acceder a muchos beneficios, como por ejemplo:\nOtras tarjetas ofrecen millas o puntos por tus consumos, pero en Lemon te regalamosBitcoin con cada compra que hagas.\n\nTambién te permite acceder a muchos beneficios, como por ejemplo:\n\nPodés usarla en cualquier país del mundo.\n\nPodés generar rendimientos poniendo a trabajar tus crypto.\n\nAcceder a preventas y descuentos exclusivos\n\n¡Y más!\n\n¿Es de débito o de crédito?\n\nNi una opción ni la otra. La Lemon Card es una tarjeta prepaga VISA. Esto quiere decir que solo va a funcionar si tiene fondos en pesos argentinos o en crypto.\n\n¿Puedo usar mi tarjeta para comprar en cuotas?\n\nAl ser una tarjeta prepaga solo podés pagar en una cuota.\n\n¿Puedo usar mi tarjeta en el exterior?\n\n¡Obvio! Cualquier comercio que esté dentro de la red VISA, va a aceptar tu Lemon Card. Para eso, necesitamos que completes el formulario que vas a encontrar en la sección Tarjeta, en el botón ⚙️.\nOtras tarjetas ofrecen millas o puntos por tus consumos, pero en Lemon te regalamosBitcoin con cada compra que hagas.\n\nTambién te permite acceder a muchos beneficios, como por ejemplo:\n\nPodés usarla en cualquier país del mundo.\n\nPodés generar rendimientos poniendo a trabajar tus crypto.\n\nAcceder a preventas y descuentos exclusivos\n\n¡Y más!\n\n¿Es de débito o de crédito?\n\nNi una opción ni la otra. La Lemon Card es una tarjeta prepaga VISA. Esto quiere decir que solo va a funcionar si tiene fondos en pesos argentinos o en crypto.\n\n¿Puedo usar mi tarjeta para comprar en cuotas?\n\nAl ser una tarjeta prepaga solo podés pagar en una cuota.\n\n¿Puedo usar mi tarjeta en el exterior?\n\n¡Obvio! Cualquier comercio que esté dentro de la red VISA, va a aceptar tu Lemon Card. Para eso, necesitamos que completes el formulario que vas a encontrar en la sección Tarjeta, en el botón ⚙️.\nTe traemos lo mejor del mundo crypto, pero con un poco de sabor a limón. 😉\n\nLemon es una app que te permite ingresar al mundo crypto y a la web 3, para pagar con una tarjeta Visa Prepaga e internacional, de manera fácil, rápida y segura.\n\n¿Qué podés hacer con Lemon?Te dejamos una lista con solo algunas de las cosas que podés hacer👇🏼\n\nPagar en comercios de Argentina, o de todo el mundo, con tu Lemon Card 💳\n\nEnviar y recibir pesos argentinos (ARS) entre cuentas emitidas en argentina\n\nComprar y vender crypto, 24/7\n\nEnviar y recibir crypto, sin horarios.\n\nPagar tus servicios con pesos o crypto\n\nTener tu perfil en web3 y tu primer Lemmy NFT\n\nPodes generar intereses semanales con Lemon Earn\n\nAcceder a preventas exclusivas y promociones 🎟😎\n\nNuestra comunidad  ya cuenta con más de 1 millón de Lemoners y queremos que vos también seas parte.\n\n¿Qué estás esperando? Dale, sumate a la revolución crypto, sumate a Lemon. 🍋",
    "urls": [
        "https://help.lemon.me/es/articles/4868375-que-es-la-lemon-card-y-donde-la-puedo-usar",
        "https://help.lemon.me/es/articles/4868375-que-es-la-lemon-card-y-donde-la-puedo-usar#main-content",
        "https://help.lemon.me/es/articles/4868375-que-es-la-lemon-card-y-donde-la-puedo-usar",
        "https://help.lemon.me/es/articles/4868375-que-es-la-lemon-card-y-donde-la-puedo-usar#main-content",
        "https://help.lemon.me/es/articles/5017731-que-es-lemon#main-content"
    ]
    }
   ```

### Notes

- The RAG system is slow when using the **llama3.2** model locally. Alternatives can improve performance.

---

## Exercise 4: Get Response

### Overview

This feature integrates intent classification and RAG to provide tailored responses. If the intent matches a predefined category, a standard response is customized. Otherwise, the RAG system is used.

### Requirements

1. **Intent Classification**: Classify user questions using the Intent Classification model.
2. **Standard Responses**: Use predefined responses from `standard_responses.json` and personalize them with the LLM.
3. **RAG Integration**: For uncategorized intents, query the RAG system.

### Execution Steps

1. **Setup Prerequisites**:
   - Ensure **Ollama** is installed and `llama3.2` is downloaded.
   - Place `standard_responses.json` in the `app/data` folder.

2. **Run the Server**:
   Start the server using:
   ```bash
   python app/main.py
   ```

3. **Get Response**:
   Send a POST request to `http://127.0.0.1:8000/response/get_response`. For example:

   **Using Standard Response**:
   ```json
   {
       "question": "¿Cómo denunciar una tarjeta perdida?"
   }
   ```
   - It is categorized as standard category: Denuncia de Tarjeta Perdida 
   - Standard answer: "Denuncia de Tarjeta Perdida": "Si perdiste tu tarjeta, por favor repórtala inmediatamente para prevenir usos no autorizados. Puedes hacerlo a través de la configuración de tu cuenta.",
   Response:
   ```json
   {
    "answer": "📝 Si perdiste tu tarjeta, puedes denunciarla inmediatamente a través de la configuración de tu cuenta. Sigue estos pasos:\n\n1. Accede a tu cuenta.\n2. Busca la sección de Perdida o Denuncia.\n3. Ingresa tus datos personales y explica la situación.\n4. Confirma que has denunciado la tarjeta.\n\n¡Listo! 🎉"
    }
   ```

   **Using RAG System**:
   ```json
   {
    "question": "¿Puedo acceder al soporte de atención al cliente por teléfono?"
    }
   ```
   - It is categorized as standard category: Otro
   Response:
   ```json
   {
    "answer": "📞 Sí, puedes acceder al soporte de atención al cliente por teléfono. 📲",
    "context": "➡️ Verificá que tenés buena señal para grabar el video.\n\n➡️ Sugerimos que utilices tus datos móviles y no el WIFI.\n\n➡️ No olvides revisar en spam el correo de autenticación.\n\nSi estos consejos impiden generar una nueva clave, escribinos asoporte@lemon.meo contactate por la app desde la sección “Necesito ayuda”.\n\n​\n\n​\n➡️ Verificá que tenés buena señal para grabar el video.\n\n➡️ Sugerimos que utilices tus datos móviles y no el WIFI.\n\n➡️ No olvides revisar en spam el correo de autenticación.\n\nSi estos consejos impiden generar una nueva clave, escribinos asoporte@lemon.meo contactate por la app desde la sección “Necesito ayuda”.\n\n​\n\n​\n¿Costos? ¿Qué es eso? 🤨\n\nPor si no quedó claro; no, no hay costos asociados a la solicitud o al mantenimiento de tu tarjeta física o virtual. ¡Son GRATIS! 🆓\n\nConocé como pedirlas desde acá:\n\nSi tenés alguna duda, escribinos asoporte@lemon.meo contactate por la app desde: \"$tulemontag\" → \"Necesito ayuda\" → \"Comunicate con soporte\".\n¿Costos? ¿Qué es eso? 🤨\n\nPor si no quedó claro; no, no hay costos asociados a la solicitud o al mantenimiento de tu tarjeta física o virtual. ¡Son GRATIS! 🆓\n\nConocé como pedirlas desde acá:\n\nSi tenés alguna duda, escribinos asoporte@lemon.meo contactate por la app desde: \"$tulemontag\" → \"Necesito ayuda\" → \"Comunicate con soporte\".\nSolicitándola a soporte a través del chat de la app\n\nCada movimiento queda registrado en el legajo de los usuarios y a fin de mes se elabora la factura correspondiente a cada período.​En caso de necesitarla, se puede solicitar a través del chat de la app ingresando porMi $lemontag > Necesito ayuda > Comunicate con soporte.",
    "urls": [
        "https://help.lemon.me/es/articles/5867270-olvide-mi-clave-o-pin-de-acceso",
        "https://help.lemon.me/es/articles/5867270-olvide-mi-clave-o-pin-de-acceso#main-content",
        "https://help.lemon.me/es/articles/10029243-existe-un-costo-de-solicitud-o-de-mantenimiento",
        "https://help.lemon.me/es/articles/10029243-existe-un-costo-de-solicitud-o-de-mantenimiento#main-content",
        "https://help.lemon.me/es/articles/5017610-hay-una-factura-o-boleto-por-compra-de-criptomonedas#main-content"
    ]
    }
   ```

### Notes

- Use the Swagger documentation at `http://localhost:8000/apidocs` to explore the API.
- Optimize performance by using alternative LLMs if required.

---
