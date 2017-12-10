"""Perform sentiment analysis on strings with the NLTK library."""
from nltk.sentiment.vader import SentimentIntensityAnalyzer

COMPOUND_KEY = "compound"
NEGATIVE_KEY = "neg"
NEUTRAL_KEY = "neu"
POSITIVE_KEY = "pos"


def get_sentence_sentiment(sentence):
    """Return dictionary with keys "compound", "neg", "neu", and "pos" whose values are the sentiment scores."""
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(sentence)
    return sentiment_scores


def get_avg_sentiment(list_of_comments):
    """Return average compound, negative, neutral, and positive sentiment of comments in a list."""

    if not list_of_comments or list_of_comments == []:
        zero_dict = {
            COMPOUND_KEY: 0,
            NEGATIVE_KEY: 0,
            NEUTRAL_KEY: 0,
            POSITIVE_KEY: 0}
        return zero_dict

    comment_counter = 0
    compound_total = 0
    negative_total = 0
    neutral_total = 0
    positive_total = 0

    for comment in list_of_comments:
        sentiment = get_sentence_sentiment(comment)
        compound_total += sentiment[COMPOUND_KEY]
        negative_total += sentiment[NEGATIVE_KEY]
        neutral_total += sentiment[NEUTRAL_KEY]
        positive_total += sentiment[POSITIVE_KEY]
        comment_counter += 1

    avg_sentiment = {COMPOUND_KEY: (compound_total / comment_counter),
                     NEGATIVE_KEY: (negative_total / comment_counter),
                     NEUTRAL_KEY: (neutral_total / comment_counter),
                     POSITIVE_KEY: (positive_total / comment_counter)}

    return avg_sentiment
