class ConfidenceCheckNode:
    def __init__(self, threshold=0.7):  # Default threshold of 70%
        self.threshold = threshold

    def check_confidence(self, confidence):
        return confidence >= self.threshold
