import torch
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification


class InferenceNode:
    def __init__(self, model_path):
        self.tokenizer = DistilBertTokenizer.from_pretrained(model_path)
        self.model = DistilBertForSequenceClassification.from_pretrained(model_path)
        self.ambiguous_phrases = {
            "okay", "fine", "not bad", "so-so", "meh",
            "could be better", "nothing special", "average", "mediocre"
        }

    def is_ambiguous(self, text):
        text_lower = text.lower()
        return any(phrase in text_lower for phrase in self.ambiguous_phrases)

    def classify(self, text):
        inputs = self.tokenizer(text, return_tensors="pt")
        with torch.no_grad():
            outputs = self.model(**inputs)

        logits = outputs.logits
        probabilities = torch.nn.functional.softmax(logits, dim=-1)
        predicted_class = torch.argmax(probabilities).item()
        confidence = probabilities[0][predicted_class].item()

        # Adjust confidence for ambiguous phrases
        if self.is_ambiguous(text):
            confidence = 0.55  # Set a lower confidence for ambiguous phrases

        return predicted_class, confidence