class FallbackNode:
    def request_clarification(self, current_sentiment, text):
        print(f"\n⚠️ Potential incorrect sentiment detected!")
        print(f"Model predicted: {current_sentiment}")
        print(f"Review text: '{text}'")
        print("Was this correct? (yes/no):")

        while True:
            response = input("Your answer: ").strip().lower()
            if response in ['yes', 'no', 'y', 'n']:
                return response.startswith('n')  # Returns True if user says no (needs correction)
            print("Please enter 'yes' or 'no'")
