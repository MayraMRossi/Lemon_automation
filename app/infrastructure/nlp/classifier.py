class Classifier:
    def classify(self, text: str) -> str:
        # Mock classification logic
        if "crypto" in text.lower():
            return "Crypto"
        elif "bank" in text.lower():
            return "Banking"
        elif "card" in text.lower():
            return "Card"
        else:
            return "Other"