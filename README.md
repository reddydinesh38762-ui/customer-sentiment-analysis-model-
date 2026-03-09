# 📊 Customer Sentiment Analysis Model

This project performs sentiment analysis on customer reviews using Python. It classifies reviews as **Positive**, **Negative**, or **Neutral** and generates a **Word Cloud** to visualize common themes in positive feedback.

## 🚀 Features
*   **Automated Sentiment Scoring:** Uses `TextBlob` to calculate polarity.
*   **Data Visualization:** Generates a Word Cloud of the most frequent positive words.
*   **Batch Processing:** Handles large datasets via CSV files.

## 🛠️ Tech Stack
*   **Python:** The core programming language.
*   **Pandas:** For data manipulation and CSV handling.
*   **TextBlob:** For Natural Language Processing (NLP) and sentiment scores.
*   **WordCloud & Matplotlib:** For creating and saving the visual analysis.

## 📁 Project Structure
```text
├── data/
│   ├── sample_reviews.csv       # Input dataset
│   └── sentiment_wordcloud.png  # Generated output visualization
├── sentiment_analysis.py        # Main Python script
├── requirements.txt             # List of dependencies
└── README.md                    # Project documentation
