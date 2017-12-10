import analyze_sentiment
from analyze_sentiment import COMPOUND_KEY
from analyze_sentiment import NEGATIVE_KEY
from analyze_sentiment import NEUTRAL_KEY
from analyze_sentiment import POSITIVE_KEY


def test_get_sentence_sentiment_for_expected_keys():
    """Check that dictionary from sentiment analysis contains compound, negative, neutral, and positive keys."""
    sentence = "I love you!"
    sentiment_dict = analyze_sentiment.get_sentence_sentiment(sentence)
    keys = list(sentiment_dict.keys())

    assert COMPOUND_KEY in keys
    assert NEGATIVE_KEY in keys
    assert NEUTRAL_KEY in keys
    assert POSITIVE_KEY in keys


def test_get_sentence_sentiment_with_positive_sentence():
    """Check that an obviously positive sentence returns a positive sentiment."""
    sentence = "I love you!"
    sentiment_dict = analyze_sentiment.get_sentence_sentiment(sentence)
    compound_value = sentiment_dict[COMPOUND_KEY]

    assert compound_value > 0


def test_get_sentence_sentiment_with_negative_sentence():
    """Check that an obviously negative sentence returns a negative sentiment."""
    sentence = "I hate you!"
    sentiment_dict = analyze_sentiment.get_sentence_sentiment(sentence)
    compound_value = sentiment_dict[COMPOUND_KEY]

    assert compound_value < 0


def test_get_avg_sentiment_with_positive_sentences():
    """Check that list of obviously positive sentences returns a positive sentiment."""
    comments = ["I love you!", "I am happy!", "You are wonderful."]
    avg_sentiment_dict = analyze_sentiment.get_avg_sentiment(comments)

    compound_value = avg_sentiment_dict[COMPOUND_KEY]

    assert compound_value > 0


def test_get_avg_sentiment_with_negative_sentences():
    """Check that list of obviously negative sentences returns a positive sentiment."""
    comments = ["I hate you!", "I am sad.", "You are awful."]
    avg_sentiment_dict = analyze_sentiment.get_avg_sentiment(comments)

    compound_value = avg_sentiment_dict[COMPOUND_KEY]

    assert compound_value < 0
