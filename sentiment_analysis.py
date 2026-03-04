from textblob import TextBlob

def analyze_sentiment(text):
    # This line calculates the sentiment score
    analysis = TextBlob(text)
    
    # Polaritiy ranges from -1 (very negative) to 1 (very positive)
    if analysis.sentiment.polarity > 0:
        return "Positive 😊"
    elif analysis.sentiment.polarity < 0:
        return "Negative 😡"
    else:
        return "Neutral 😐"

# Test the model
feedback = input("Enter customer feedback: ")
result = analyze_sentiment(feedback)
print(f"Analysis Result: {result}")
