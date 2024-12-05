import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from langchain.text_splitter import RecursiveCharacterTextSplitter
from app.infrastructure.vector_store.chroma_vector_store import ChromaVectorStore
import uuid
import os

def scrape_and_populate_vector_store(base_url: str, collection_name: str):
    """
    Scrapes a website and populates its content into a vector store.
    """
    visited_urls = set()  # Keeps track of visited URLs

    # Define la ruta raíz
    root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app/data'))
    print(f"Root path: {root_path}")
    vector_store_path = os.path.join(root_path, 'vector_store')

    vector_store = ChromaVectorStore(collection_name=collection_name, path=vector_store_path)
    vector_store.clear_collection()  # Clear the collection before populating new data

    def scrape_page(url: str):
        if url in visited_urls:
            print(f"URL already visited: {url}")
            return  # Skip if the URL has already been processed

        visited_urls.add(url)
        print(f"Processing page: {url}")

        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return

        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract page content (title and paragraphs)
        title = soup.title.string.strip() if soup.title else "No Title"
        content = []

        for paragraph in soup.find_all('p'):
            text = paragraph.get_text(strip=True)
            if text:
                content.append(text)

        if content:
            # Split content into chunks using langchain's text splitter
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            chunks = text_splitter.split_text("\n\n".join(content))

            # Debugging: check number of chunks
            print(f"Chunks for URL {url}: {len(chunks)} chunks")

            # Add chunks to vector store with metadata
            documents = chunks  # documents is already a list
            ids = [str(uuid.uuid4()) for _ in range(len(chunks))]  # Generate unique IDs for each chunk
            metadatas = [{"url": url, "title": title} for _ in range(len(chunks))]  # Metadata for each chunk

            # Ensure documents and metadata are lists
            vector_store.add_documents(documents=documents, metadatas=metadatas)
            print(f"Processed and added content from: {url}")
        else:
            print(f"Skipped {url} (No content found)")

        # Follow links recursively (relative URLs)
        for link in soup.find_all('a', href=True):
            href = link['href']
            full_url = urljoin(url, href)
            if full_url.startswith(base_url) and full_url not in visited_urls:
                scrape_page(full_url)

    # Start scraping from the base URL
    scrape_page(base_url)
    print("Scraping and vector store population completed.")

if __name__ == "__main__":
    base_url = 'https://help.lemon.me/es/'  # Base URL of the help center
    collection_name = 'help_center'
    print(f"Starting scraping and population for: {base_url}")
    scrape_and_populate_vector_store(base_url, collection_name)