#import sys
import os
import re
# local imports
import analyze_sentiment
import gg_gensim
from analyze_comments import embed_stats_into_html


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
        response = get_reflection(File)
        # perform and print sentiment analysis
        RESPONSES.append(response)
    sentiment = analyze_sentiment.get_sentence_sentiment(RESPONSES[0])
    print(sentiment)
    embed_stats_into_html(str(sentiment))
    gg_gensim.gensim_analysis(RESPONSES)


def get_reflection(file_path):
    """ reads through and creates a list of lists from inputted file """
    with open(file_path, 'r') as reflection:
        # to add additional file types just use the .endswith() function to
        # specifiy the file type then add in how the file should be broken up
        # into a list with the .split() function or whatever functionality is
        # needed
        if file_path.endswith(".md"):
            # removes newline characters and breaks up file into sentences
            content = reflection.read()
            # removes special characters
            content = re.sub(r'[^a-zA-Z0-9\*\^\(\)\'\-\n\.]', ' ', content)
            content.split('. ')
    return content  # list
