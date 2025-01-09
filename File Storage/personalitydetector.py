import tweepy
import re
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Set up Twitter API credentials
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET" 

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, version="2")

# Define function to preprocess tweets
def preprocess_tweet(tweet):
    # Remove URLs
    tweet = re.sub(r"http\S+", "", tweet)
    # Remove mentions
    tweet = re.sub(r"@\S+", "", tweet)
    # Remove special characters
    tweet = re.sub(r"[^a-zA-Z0-9]+", " ", tweet)
    # Convert to lowercase
    tweet = tweet.lower()
    # Tokenize
    tokens = nltk.word_tokenize(tweet)
    # Remove stop words
    stop_words = set(stopwords.words("english"))
    filtered_tokens = [token for token in tokens if token not in stop_words]
    # Join tokens back into a string
    filtered_tweet = " ".join(filtered_tokens)
    return filtered_tweet

# Define function to collect tweets for a user
def collect_tweets(username):
    tweets = []
    for tweet in api.user_timeline(username, tweet_mode="extended"):
        tweets.append(tweet.full_text)
    return tweets

# Define function to extract features from tweets data
def extract_features(tweets):
    # Preprocess tweets
    preprocessed_tweets = [preprocess_tweet(tweet) for tweet in tweets]
    # Extract features using TF-IDF vectorizer
    vectorizer = TfidfVectorizer()
    features = vectorizer.fit_transform(preprocessed_tweets)
    return features

# Define function to train machine learning model
def train_model(features, labels):
    # Split data into training and testing sets
    x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)    # Train Random Forest Classifier
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(x_train, y_train)
    # Evaluate model on testing set
    accuracy = clf.score(x_test, y_test)
    print("Accuracy:", accuracy)
    return clf


