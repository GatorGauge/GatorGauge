#import sys
import os
# local imports
import analyze_sentiment
import parse_comments
import get_reflection
import get_list_of_commits
import analyze_java
import java_to_string
import gg_gensim


def analyze_commits(out):
    """ analyze commits """
    repo_list = next(os.walk("./" + str(out)))[1]
    for repo in repo_list:
        print("\nCommits for " + str(repo) + ": ")
        commits = get_list_of_commits.get_list_of_commits(
            "./" + str(out) + "/" + str(repo))
        print(*commits, end="\n")
        print("\nSentiment Analysis for " + str(repo) + ": ")
        print(analyze_sentiment.get_sentence_sentiment(str(commits)))

    gg_gensim.gensim_analysis(commits)


def analyze_reflection(out):
    """ analyze reflections """
    LISTFILES = list()
    for subdir, dirs, files in os.walk("./" + str(out)):
        for file in files:
            if file.endswith("reflection.md"):
                LISTFILES.append(os.path.join(subdir, file))
    if not LISTFILES:
        print("ERROR: File 'reflection.md' does not exist")
    RESPONSES = list()
    for File in LISTFILES:
        response = get_reflection.get_reflection(File)
        # perform and print sentiment analysis
        responses.append(response)
    print(analyze_sentiment.get_sentence_sentiment(responses[0]))
    gg_gensim.gensim_analysis(responses)
