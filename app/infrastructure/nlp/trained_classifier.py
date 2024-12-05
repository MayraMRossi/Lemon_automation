import joblib
class TrainedClassifier:
    def __init__(self, model_path, vectorizer_path):
        self.model = joblib.load(model_path)
        self.vectorizer = joblib.load(vectorizer_path)
    def classify(self, question: str) -> str:
        question_vector = self.vectorizer.transform([question])
        category = self.model.predict(question_vector)
        return category[0]
