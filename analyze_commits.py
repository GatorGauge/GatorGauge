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
    write_string = "Number of commits: " + str(len(return_list)) + "\n"
    num_commits = len(return_list)

    sentiment = get_avg_sentiment(return_list)
    
    emojis_count = get_emojis_count(return_list)
    for key, value in emojis_count.items():
        write_string += str(key) + ": " + str(value) + "\n"
        html_write_string += "</br><b>" + str(key) + ":</b> " + str(value)
    print(write_string)

    #format results for HTLM embedding
    html_write_string = "<b>Number of commits: </b>" + str(len(returnlist)) + \
        "<b>Average Sentiment: </b>" + str(sentiment) + \
        "<b>Emojis Count: </b>" + str(emojis_count)
    embed_stats_into_html(html_write_string)

   
    gg_gensim.gensim_analysis(return_list)

