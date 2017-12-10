import sys
import os
# local imports
import analyze_sentiment
import parse_comments
import get_reflection
import get_list_of_commits
import analyze_java
import java_to_string

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
    
def analyze_comments():
    """ analyze comments """
    with open('./java/HelloWorld.java', 'r') as java_file:
        JAVA_STRING = java_file.read()

    COMMENTS = parse_comments.list_singleline_java_comments(JAVA_STRING)
    print("\nSingleline comments\n-------------------")
    for comment in COMMENTS:
        print(repr(comment))
    print("Number of singleline comments: " +
          str(parse_comments.count_singleline_java_comments(JAVA_STRING)))

    print("Ratio of singleline comments to total Java source code lines: " +
          str(parse_comments.get_ratio_of_singleline_comments_to_source_code(JAVA_STRING)))

    COMMENTS = parse_comments.list_multiline_java_comments(JAVA_STRING)
    print("\nMultiline comments\n------------------")
    for comment in COMMENTS:
        print(repr(comment))
    print("Number of multiline comments: " +
          str(parse_comments.count_multiline_java_comments(JAVA_STRING)))

    print("Ratio of multiline comments to total Java source code lines: " +
str(parse_comments.get_ratio_of_multiline_comments_to_source_code(JAVA_STRING)))
    print("Sentiment analysis on single-line comments:")
    print(analyze_sentiment.get_avg_sentiment(parse_comments.list_singleline_java_comments(JAVA_STRING)))
    print("Sentiment analysis on multi-line comments:")
    print(analyze_sentiment.get_avg_sentiment(parse_comments.list_multiline_java_comments(JAVA_STRING)))

    #TODO: topic analysis on Java Docstrings

def analyze_commits(out):
    """ analyze commits """
    repo_list = next(os.walk("./" + str(out)))[1]
    for repo in repo_list:
        print("\nCommits for "+str(repo)+": ")
        commits = get_list_of_commits.get_list_of_commits("./"+str(out)+"/"+str(repo))
        print(*commits,end="\n")
        print("\nSentiment Analysis for "+str(repo)+": ")
        print(analyze_sentiment.get_sentence_sentiment(str(commits)))
    
    #TODO: topic analysis
    

def analyze_reflection(out):
    """ analyze reflections """
    listFiles = list()
    for subdir, dirs, files in os.walk("./" + str(out)):
        for file in files:
            if file.endswith("reflection.md"):
                listFiles.append(os.path.join(subdir, file))
    if len(listFiles) == 0:
        print("ERROR: File 'reflection.md' does not exist")
    responses = list()
    for File in listFiles:
        response = get_reflection.get_reflection(File)
        # perform and print sentiment analysis
        print(response)
        print(analyze_sentiment.get_sentence_sentiment(response))
        responses.append(response)
    
    #TODO: topic analysis

