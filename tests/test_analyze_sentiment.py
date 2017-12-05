import analyze_sentiment

COMPOUND_KEY = "compound"
NEGATIVE_KEY = "neg"
NEUTRAL_KEY = "neu"
POSITIVE_KEY = "pos"


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
