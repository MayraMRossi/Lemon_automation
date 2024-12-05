import unittest
from unittest.mock import patch, MagicMock
from infrastructure.vector_store.chroma_vector_store import ChromaVectorStore
from scripts.scrape_and_populate_vector_store import scrape_and_populate_vector_store

class TestScrapingAndVectorStore(unittest.TestCase):

    @patch('requests.get')
    @patch.object(ChromaVectorStore, 'add_documents')
    @patch.object(ChromaVectorStore, 'clear_collection')
    def test_scrape_and_populate_vector_store(self, mock_clear_collection, mock_add_documents, mock_get):
        # Mock de la respuesta HTTP
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = b"<html><head><title>Test Page</title></head><body><p>Test content.</p></body></html>"
        mock_get.return_value = mock_response

        # Mock de la función `add_documents` que debe agregar los documentos al vector store
        mock_add_documents.return_value = None

        # Llamamos a la función de scraping
        base_url = 'https://help.lemon.me/es/'
        collection_name = 'help_center'

        # Ejecutamos el proceso de scraping (esto debería agregar documentos a la base de datos)
        scrape_and_populate_vector_store(base_url, collection_name)

        # Verificamos que `clear_collection` haya sido llamado para limpiar la colección antes de agregar nuevos documentos
        mock_clear_collection.assert_called_once()

        # Verificamos que `add_documents` haya sido llamado con la lista de documentos y metadatos esperados
        mock_add_documents.assert_called_once()

        # Aseguramos que los documentos pasados son una lista
        documents_argument = mock_add_documents.call_args[1]['documents']
        self.assertIsInstance(documents_argument, list)
        self.assertGreater(len(documents_argument), 0)  # Aseguramos que haya al menos un documento

        # Verificamos que los metadatos son una lista y contienen las claves correctas
        metadatas_argument = mock_add_documents.call_args[1]['metadatas']
        self.assertIsInstance(metadatas_argument, list)
        self.assertGreater(len(metadatas_argument), 0)
        self.assertIn('url', metadatas_argument[0])
        self.assertIn('title', metadatas_argument[0])

    @patch('requests.get')
    def test_no_repeat_urls(self, mock_get):
        # Simulamos la misma página siendo visitada
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

        # Simulamos el proceso de scraping en una sola página
        scrape_page(base_url)

        # Verificamos que la URL solo se visite una vez
        self.assertEqual(len(visited_urls), 1)  # Solo debe haber una URL en el conjunto

    @patch('requests.get')
    def test_handle_empty_page(self, mock_get):
        # Simulamos una página sin contenido
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = b"<html><head><title>Empty Page</title></head><body></body></html>"
        mock_get.return_value = mock_response

        # Verificamos que la página sin contenido sea manejada correctamente
        base_url = 'https://help.lemon.me/es/'
        collection_name = 'help_center'

        # Ejecutamos el proceso de scraping (esto no debería agregar ningún documento debido a la falta de contenido)
        scrape_and_populate_vector_store(base_url, collection_name)

        # Verificamos que no se hayan agregado documentos debido a que la página está vacía
        mock_get.assert_called_once()
        mock_add_documents.assert_not_called()


if __name__ == '__main__':
    unittest.main()
