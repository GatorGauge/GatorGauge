"""Execute analysis for commits."""
import os


from emoji_library import get_emojis_count
from analyze_sentiment import get_avg_sentiment
import parse_commits
import gg_gensim
from analyze_comments import embed_stats_into_html
from dulwich import porcelain


def analyze_commits(out):
    """Execute analysis for commits."""   
    return_list = []
    return_list = get_list_of_commits(out)
    write_string = ""
    print("Number of commits: " + str(len(return_list)))
    write_string += "Number of commits: " + str(len(return_list))

    gg_gensim.gensim_analysis(return_list)

    sentiment = get_avg_sentiment(return_list)
    for key, value in sentiment.items():
        print(key, value)
        write_string += str(key) + ", " + str(value) + "\n"

    emojis_count = get_emojis_count(return_list)
    for key, value in emojis_count.items():
        print(key, value)
        write_string += str(key) + ", " + str(value) + "\n"
    print(write_string)
    # embed_stats_into_html(write_string)
    
    
def get_list_of_commits(out):
    """Write a list of commit messages."""
    repo_list = next(os.walk("./" + str(out)))[1]
    return_list = []
    for repo in repo_list:
        with porcelain.open_repo_closing("./" + str(out) + "/"+ str(repo)) as repo:
            walker = repo.get_walker(reverse=True)
        for entry in walker:
            item = str(entry.commit.message.decode())
            item = item.replace("\n", "")
            return_list.append(item)
    return return_list
