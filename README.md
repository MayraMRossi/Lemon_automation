
## Execution Instructions

### 1. Environment Setup
Clone the repository:
```bash
git clone https://github.com/your-username/lemon-cx-automation.git
cd lemon-cx-automation
```

Install dependencies:
```bash
pip install -r requirements.txt
```

### 2. Ollama Setup
Install Ollama:
```bash
curl https://ollama.ai/install.sh | sh
```

Start Ollama with Llama 3.2:
```bash
ollama start llama3.2
```

### 3. Running Scripts
#### a. Email Processing
Run the script to process emails:
```bash
python main.py
```
Check the `data/processed_emails.csv` file for results.

#### b. Intent Classification Model Training
Run the script to train the model:
```bash
python scripts/train_model.py
```
The trained model and vectorizer will be saved in the `models/` directory.

#### c. Populate Vector Database
Run the script to populate the vector database with help center data:
```bash
python scripts/populate_vector_store.py
```

#### d. Web Scraping
Run the web scraper to collect data from the Lemon help center:
```bash
python scripts/web_scraper.py
```
The scraped data will be saved in the `data/lemon_help_center` directory as individual Markdown files.

#### e. Run Flask Server
Start the Flask server:
```bash
python main.py
```
Access the API at `http://localhost:8000`.

### 4. Docker Setup
Build the Docker image:
```bash
docker-compose build
```

Run the Docker container:
```bash
docker-compose up
```

### 5. Running Tests
Run the tests:
```bash
pytest tests/
```

### 6. Using the API
#### a. Intent Classification
Send a POST request to `/intents/classify` with the following body:
```json
{
  "question": "How do I withdraw my funds in cryptocurrencies?"
}
```

#### b. RAG Query
Send a POST request to `/rag/query` with the following body:
```json
{
  "query": "How can I withdraw my funds?"
}
```
