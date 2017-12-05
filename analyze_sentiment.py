"""Perform sentiment analysis on strings with the NLTK library."""
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def get_sentence_sentiment(sentence):
    """Return dictionary with keys "compound", "neg", "neu", and "pos" whose values are the sentiment scores."""
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(sentence)
    return sentiment_scores
