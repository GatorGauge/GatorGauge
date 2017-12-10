import sys
import os
# local imports
import analyze_sentiment
import parse_comments
import get_reflection
import get_list_of_commits
import analyze_java

def analyze_source():
    """ analyze source code """
    print("SOURCE")
    
    
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

def analyze_commits(out):
    """ analyze commits """
    repo_list = next(os.walk("./" + str(out)))[1]
    for repo in repo_list:
        print("\nCommits for "+str(repo)+": ")
        commits = get_list_of_commits.get_list_of_commits("./"+str(out)+"/"+str(repo))
        print(*commits,end="\n")
        print("\nSentiment Analysis for "+str(repo)+": ")
        print(analyze_sentiment.get_sentence_sentiment(str(commits)))

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
    # for res in responses:
        # print(res)

