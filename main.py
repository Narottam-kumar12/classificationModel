from inference_node import InferenceNode
from confidence_check_node import ConfidenceCheckNode
from fallback_node import FallbackNode
from custom_logger import log_event

SENTIMENT_MAP = {0: "Negative", 1: "Positive"}


def main():
    model_name = 'distilbert-base-uncased-finetuned-sst-2-english'
    threshold = 0.7  # Confidence threshold

    inference_node = InferenceNode(model_name)
    confidence_check_node = ConfidenceCheckNode(threshold)
    fallback_node = FallbackNode()

    print("Sentiment Analysis System (type 'exit' to quit)\n")
    print("=" * 50)

    while True:
        try:
            user_input = input("\nEnter a review: ").strip()
            if user_input.lower() == 'exit':
                print("\nExiting...")
                break
            if not user_input:
                continue

            # Get initial prediction
            predicted_label, confidence = inference_node.classify(user_input)
            sentiment = SENTIMENT_MAP.get(predicted_label, "Unknown")

            # Check confidence threshold
            if confidence_check_node.check_confidence(confidence):
                print(f"\nPredicted sentiment: {sentiment} | Confidence: {confidence:.2f}")
            else:
                print(f"\n⚠️ Low confidence prediction ({confidence:.2f})")
                if fallback_node.request_clarification(sentiment, user_input):
                    clarified_input = input("\nPlease clarify your review: ").strip()
                    if clarified_input.lower() == 'exit':
                        break

                    predicted_label, confidence = inference_node.classify(clarified_input)
                    final_sentiment = SENTIMENT_MAP.get(predicted_label, "Unknown")

                    print(f"\n✅ Final sentiment: {final_sentiment}")
                else:
                    print(f"\nKeeping original prediction: {sentiment}")

            print("\n" + "=" * 50)

        except KeyboardInterrupt:
            print("\nExiting...")
            break


if __name__ == "__main__":
    main()
