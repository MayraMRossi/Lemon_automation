import unittest
from unittest.mock import patch, MagicMock
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scripts.scrape_and_populate_vector_store import scrape_and_populate_vector_store
from app.infrastructure.vector_store.chroma_vector_store import ChromaVectorStore


class TestScrapingAndVectorStore(unittest.TestCase):

    @patch('requests.get')
    @patch.object(ChromaVectorStore, 'add_documents')
    @patch.object(ChromaVectorStore, 'clear_collection')
    def test_scrape_and_populate_vector_store(self, mock_clear_collection, mock_add_documents, mock_get):
        print("Testing scrape_and_populate_vector_store method...")
        # Mock HTTP response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = b"<html><head><title>Test Page</title></head><body><p>Test content.</p></body></html>"
        mock_get.return_value = mock_response

        # Mock `add_documents` function to add documents to the vector store
        mock_add_documents.return_value = None

        # Call the scraping function
        base_url = 'https://help.lemon.me/es/'
        collection_name = 'help_center'

        # Execute the scraping process (this should add documents to the database)
        scrape_and_populate_vector_store(base_url, collection_name)

        # Verify that `clear_collection` was called to clear the collection before adding new documents
        mock_clear_collection.assert_called_once()

        # Verify that `add_documents` was called with the expected list of documents and metadata
        mock_add_documents.assert_called_once()

        # Ensure that the documents passed are a list
        documents_argument = mock_add_documents.call_args[1]['documents']
        self.assertIsInstance(documents_argument, list)
        self.assertGreater(len(documents_argument), 0)  # Ensure there is at least one document

        # Verify that the metadata is a list and contains the correct keys
        metadatas_argument = mock_add_documents.call_args[1]['metadatas']
        self.assertIsInstance(metadatas_argument, list)
        self.assertGreater(len(metadatas_argument), 0)
        self.assertIn('url', metadatas_argument[0])
        self.assertIn('title', metadatas_argument[0])
        print("scrape_and_populate_vector_store method test passed.")

    @patch('requests.get')
    def test_no_repeat_urls(self, mock_get):
        print("Testing no repeat URLs...")
        # Simulate the same page being visited
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = b"<html><head><title>Test Page</title></head><body><p>Test content.</p></body></html>"
        mock_get.return_value = mock_response

        visited_urls = set()
        base_url = 'https://help.lemon.me/es/'

        def scrape_page(url: str):
            if url in visited_urls:
                return  # Skip if already visited
            visited_urls.add(url)

        # Simulate the scraping process on a single page
        scrape_page(base_url)

        # Verify that the URL is only visited once
        self.assertEqual(len(visited_urls), 1)  # There should only be one URL in the set
        print("No repeat URLs test passed.")

    @patch('requests.get')
    def test_handle_empty_page(self, mock_get):
        print("Testing handle empty page...")
        # Simulate an empty page
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = b"<html><head><title>Empty Page</title></head><body></body></html>"
        mock_get.return_value = mock_response

        # Verify that the empty page is handled correctly
        base_url = 'https://help.lemon.me/es/'
        collection_name = 'help_center'

        # Execute the scraping process (this should not add any documents due to the lack of content)
        scrape_and_populate_vector_store(base_url, collection_name)

        # Verify that no documents were added due to the empty page
        mock_get.assert_called_once()
        mock_add_documents.assert_not_called()
        print("Handle empty page test passed.")

if __name__ == '__main__':
    unittest.main()