"""Execute analysis for commits."""

from emoji_library import get_emojis_count
from analyze_sentiment import get_avg_sentiment


def analyze_commits(list_of_commits):
    """Execute analysis for commits."""

    print("Number of commits: " + len(list_of_commits))

    # add topical analysis

    sentiment = get_avg_sentiment(list_of_commits)
    for key, value in sentiment.iteritems():
        print(key, value)

    emojis_count = get_emojis_count(list_of_commits)
    for key, value in emojis_count.iteritems():
        print(key, value)
