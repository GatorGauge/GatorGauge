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


def analyze_source(out):
    """ analyze source code """
    java_files = analyze_java.get_file_paths(".java", out)
    repoDict = dict()
    for f in java_files:
        # The second replace is so that code doesn't break on windows
        currFile = f.replace(out, "").replace("\\", "/")
        repo = currFile.split("/")[1]
        if repo in repoDict:
            continue
        files = []
        for javaFile in java_files:
            if repo in javaFile:
                files.append(javaFile)
        repoDict[repo] = files

    java_strings = []

    for key, values in repoDict.items():
        java_string = []
        for value in values:
            java_string.append(java_to_string.read_and_convert(value))
        java_strings.append(' '.join(java_string))

    analyze_java.analyze_java(java_strings)


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
        RESPONSES.append(response)
    print(analyze_sentiment.get_sentence_sentiment(RESPONSES[0]))
    gg_gensim.gensim_analysis(RESPONSES)
