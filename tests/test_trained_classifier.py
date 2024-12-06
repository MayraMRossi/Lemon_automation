import unittest
from unittest.mock import patch
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from infrastructure.nlp.trained_classifier import TrainedClassifier
from utils.exceptions import ModelLoadingError, ClassificationError

class TestTrainedClassifier(unittest.TestCase):
    @patch('joblib.load')
    def test_classify(self, mock_joblib_load):
        print("Testing classify method...")
        mock_model = mock_joblib_load.return_value
        mock_model.predict.return_value = ['Retiros Crypto']

        classifier = TrainedClassifier(model_path='dummy_path', vectorizer_path='dummy_path')
        question = "¿Cómo retiro mis fondos en criptomonedas?"
        category = classifier.classify(question)

        self.assertEqual(category, "Retiros Crypto")
        print("classify method test passed.")

    @patch('joblib.load')
    def test_classify_with_error(self, mock_joblib_load):
        print("Testing classify method with error...")
        mock_model = mock_joblib_load.return_value
        mock_model.predict.side_effect = Exception("Classification error")

        classifier = TrainedClassifier(model_path='dummy_path', vectorizer_path='dummy_path')
        question = "¿Cómo retiro mis fondos en criptomonedas?"

        with self.assertRaises(ClassificationError):
            classifier.classify(question)
        print("classify method with error test passed.")

    @patch('joblib.load')
    def test_model_loading_error(self, mock_joblib_load):
        print("Testing model loading error...")
        mock_joblib_load.side_effect = Exception("Model loading error")

        with self.assertRaises(ModelLoadingError):
            TrainedClassifier(model_path='dummy_path', vectorizer_path='dummy_path')
        print("Model loading error test passed.")

if __name__ == "__main__":
    unittest.main()