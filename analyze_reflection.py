#import sys
import os
# local imports
import analyze_sentiment
import gg_gensim


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
