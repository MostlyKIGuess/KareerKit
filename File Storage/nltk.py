import nltk

def get_sentiment(tweet):
    """Extracts the sentiment of a tweet."""

    sentiment = nltk.sentiment.SentimentAnalyzer()
    return sentiment.polarity_scores(tweet)

data = {
    'tweets': [
        "I love sunny days!",
        "I hate rainy days!",
        "I'm feeling neutral about today."
    ]
}

# Extract the sentiment of each tweet
sentiments = []
for tweet in data['tweets']:
    sentiments.append(get_sentiment(tweet))
