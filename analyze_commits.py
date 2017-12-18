"""Execute analysis for commits."""
from emoji_library import get_emojis_count
from analyze_sentiment import get_avg_sentiment
from parse_commits import get_list_of_commits
import gg_gensim
from analyze_comments import embed_stats_into_html


def analyze_commits(out):
    """Execute analysis for commits."""
    return_list = []
    return_list = get_list_of_commits(out)
    write_string = ""
    write_string += "Number of commits: " + str(len(return_list)) + "\n"

    sentiment = get_avg_sentiment(return_list)
    for key, value in sentiment.items():
        write_string += str(key) + ", " + str(value) + "\n"

    emojis_count = get_emojis_count(return_list)
    for key, value in emojis_count.items():
        write_string += str(key) + ", " + str(value) + "\n"
    print(write_string)

    #format results for HTLM embedding
    embed_string = "<b>Number of commits: </b>" + str(len(returnlist)) + \
        "<b>Average Sentiment: </b>" + str(sentiment) + \
        "<b>Emojis Count: </b>" + str(emojis_count)
    embed_stats_into_html(embed_string)
