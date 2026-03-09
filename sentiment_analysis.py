import pandas as pd
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 1. Load data
df = pd.read_csv('sample_reviews.csv')
def get_sentiment(text):
    analysis = TextBlob(str(text))
    return "Positive" if analysis.sentiment.polarity > 0 else "Negative" if analysis.sentiment.polarity < 0 else "Neutral"

df['Sentiment'] = df['Review'].apply(get_sentiment)

# 2. Generate Word Cloud for Positive Reviews
positive_text = " ".join(review for review in df[df.Sentiment == 'Positive'].Review)
wordcloud = WordCloud(background_color="white").generate(positive_text)

# 3. Save the visualization
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.savefig('data/sentiment_wordcloud.png')
print("✅ Success! Analysis and WordCloud saved in the data/ folder.")
