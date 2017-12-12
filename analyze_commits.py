"""Execute analysis for commits."""
import os

from emoji_library import get_emojis_count
from analyze_sentiment import get_avg_sentiment
from dulwich import porcelain


def analyze_commits(out):
    """Execute analysis for commits."""
    repo_list = next(os.walk("./" + str(out)))[1]
    for repo in repo_list:     
        return_list = []
        with porcelain.open_repo_closing("./" + str(out) + "/" + str(repo)) as repo:
            walker = repo.get_walker(reverse=True)
        for entry in walker:
            item = str(entry.commit.message.decode())
            item = item.replace("\n", "")
            return_list.append(item)

        print("Number of commits: " + str(len(return_list)))

        # add topical analysis

        sentiment = get_avg_sentiment(return_list)
        for key, value in sentiment.items():
            print(key, value)

        emojis_count = get_emojis_count(return_list)
        for key, value in emojis_count.items():
            print(key, value)
