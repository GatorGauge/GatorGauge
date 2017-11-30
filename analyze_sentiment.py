"""Perform sentiment analysis on strings with the NLTK library."""
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def get_sentence_sentiment(sentence):
    """Return dictionary with keys "compound", "neg", "neu", and "pos" whose values are the sentiment scores."""
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(sentence)
    return sentiment_scores


if __name__ == "__main__":
    sentences = ["I love you!",
                 "I hate you!",
                 "This is a multi-sentence sentence.\nIt should be neutral."
                 ]
    for sentence in sentences:
        sentiment_scores = get_sentence_sentiment(sentence)
        print(sentence)
        for sentiment_name in sorted(sentiment_scores):
            print("{0}: {1}".format(sentiment_name, sentiment_scores[sentiment_name]))
