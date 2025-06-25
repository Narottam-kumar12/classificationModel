Setiment Analysis System

🧠 Overview

This project implements a robust Sentiment Analysis System built using a fine-tuned DistilBERT model. 
It classifies text reviews as positive or negative, with an intelligent self-correcting fallback mechanism for ambiguous or low-confidence predictions.
This system is ideal for applications requiring real-time sentiment feedback with user interaction and correction for improved accuracy.

✅ Features

  🔍 Sentiment Classification :   Detects positive or negative sentiment in English reviews.

  ⚖️ Confidence Thresholding :    Flags predictions with low confidence for review.

  🙋 User Clarification Loop :    Allows human-in-the-loop correction for uncertain predictions.

  🧾 Logging :                    Records predictions, confidences, and user corrections.

  💻 Interactive CLI :            Command-line interface for user testing and feedback.

   ⚙️ Customizable Settingsn :      Easily configurable model and logging parameters.

Install dependencies
pip install -r requirements.txt

💬 Sample Interaction:

Enter a review: I love this product!

Predicted sentiment: Positive | Confidence: 0.98

Enter a review: It was okay

⚠️ Low confidence prediction (0.55)

⚠️ Potential incorrect sentiment detected!

Model predicted: Positive

Review text: 'It was okay'

Was this correct? (yes/no):

Your answer: no

Please clarify your review: It was mediocre

✅ Final sentiment: Negative

🗂️ File Structure

classificationModel/

├── main.py                   # Main CLI interface

├── inference_node.py         # Model prediction logic

├── confidence_check_node.py  # Handles threshold validation

├── fallback_node.py          # Collects user feedback

├── custom_logger.py          # Logging module

├── config.py                 # Configuration parameters

├── requirements.txt          # Dependencies

└── logs/                     # Logged predictions and feedback

🧬 Model Specifications

.........................................................................................................

Parameter --->	Value

Base Model --->	distilbert-base-uncased-finetuned-sst-2-english

Training Dataset --->	Stanford Sentiment Treebank (SST-2)

Accuracy  --->	~91.3% on test data

Max Tokens --->	512

Avg. Inference --->	~50ms per review (on CPU)

.........................................................................................................

📈 Performance

✅ Strong Reviews (clear positive/negative): ~98% accurate

⚠️ Ambiguous Reviews (neutral, mixed tone): ~72% accurate

     - Triggers fallback for:
     
    -  Neutral phrases: "It was okay"
    
    - Mixed sentiment: "Good but not great"

    
    -   Negations    : "Not bad"


🚫 Limitations

🌐 Only supports English language

😅 Struggles with sarcasm, irony, and complex negations

📦 No batch processing (yet)

📊 No dashboard or visual analytics

..............................................................................

🔮 Future Enhancements

🌍 Multi-language support

😐 Add neutral sentiment classification

🌐 Web-based front-end with Flask/Streamlit

🔁 Auto model retraining with user feedback

📊 Sentiment intensity scoring (very positive → very negative)

#Demo video

link ---> https://drive.google.com/file/d/1Xhb2EDrahEusn3U6AYG2Z2Q_WzSv6Io-/view?usp=drivesdk



