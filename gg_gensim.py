"""Analyze the responses to the GatorGauge evaluation using Gensim."""

# Portions of this code were taken from https://github.com/Edurate/edurate

import logging
import warnings
import gensim
from gensim import *
from profanity import profanity
from stop_words import get_stop_words
from six import viewitems
from colorama import Fore, Style
import pyLDAvis
import pyLDAvis.gensim
import webbrowser
import inspect
import os
import time

def list_of_lists(content):
    """Makes a list of lists for gensim"""
    for line in content:
        # if filePath.endswith('README.md'): # formats README.md output, uncomment if needed
            # line = re.sub(r'(?s)(#)(.*?)(  )', '', line).strip()  # annoying
            # line, removes section headers from README.md files
        nextLine = list()
        if not line == '' and '#' not in line:  # removes unnecessary lines and headers
            nextLine.append(line)
            gensim_list.append(nextLine)
    return gensim_list  # list of lists

def flip_responses(gensim_list):
    """Switch rows and columns in a list of lists."""
    if gensim_list == []:
        logging.error("Empty list given. No rows and columns to flip. Returning empty list.")
        return []

    if gensim_list is None:
        logging.error("No list given to flip. Returning None.")
        return None

    # get the number of fields in each response to create that many lists
    num_of_fields = len(gensim_list[0])

    list_of_field_responses = [[] for i in repeat(None, num_of_fields)]
    for response in gensim_list:
        for field_index, field in enumerate(response):
            list_of_field_responses[field_index].append(field)

    print(list_of_field_responses)
    return list_of_field_responses


def gensim_analysis(list_responses):
    """Complete the analysis for each answer."""
    warnings.filterwarnings('ignore')
    tokens = create_tokens(list_responses)
    dictionary = dictionary_create(tokens)
    corpus = [dictionary.doc2bow(token) for token in tokens]
    #print(corpus)
    vis = corp_eval(dictionary, tokens, corpus)
    show_vis(vis)
    time.sleep(1)
    logging.info("Analyzes gensim and returns the repeated words")


def create_tokens(list_responses):
    """Take in the list of responses and make each word a token."""
    logging.info("Creating tokens")
    stoplist = get_stop_words('en')
    tokens = []
    for res in list_responses:
        temp = []
        for word in res:
            word = word.split()
            #print(word)
            for word in word:
                word = word.lower()
                if not isinstance(word, int):
                    if not profanity.contains_profanity(word):
                        if word not in stoplist:
                            if word != "I":
                                #print(word)
                                temp.append(word)
                                #print(temp)
        tokens.append(temp)

    #print(tokens)
    return tokens


def dictionary_create(tokens):
    """Create the dictionary from the tokens of the answer."""
    dictionary = corpora.Dictionary(tokens)

    logging.info("Created a dictionary using the tokens")
    return dictionary


def corp_eval(dictionary, tokens, corpus):
    """Evaluate the corpus and produce gensim visualization."""
    i = len(tokens)
    lda = gensim.models.ldamodel.LdaModel(
        corpus,
        id2word=dictionary,
        num_topics=3,
        passes=3,
        alpha='symmetric',
        eta=None)
    logging.debug(dictionary.token2id)
    logging.debug(viewitems(dictionary.dfs))

    print(lda)
    vis = pyLDAvis.gensim.prepare(lda, corpus, dictionary)
    print(Fore.YELLOW + "These are the current topics: " + Style.RESET_ALL)
    print(lda.print_topics(i))
    return(vis)


def show_vis(vis):
    # Writing HTML of visualization to file instead of showing with pyLDAvis show function
    # because the show function starts a server, which allows only one file to be displayed
    # at once.
    print(Fore.CYAN +
          "Opening up visualization in a new tab in the browser...",
          Style.RESET_ALL)
    vis_html_text = pyLDAvis.prepared_data_to_html(vis)
    vis_html_file_name = "vis.html"
    vis_html_file = open(vis_html_file_name, "w")
    vis_html_file.write(vis_html_text)

    # Getting path to the refl_gensim.py module, which is in the same directory
    # as the HTML file. This path will be used to generate the file path to the HTML
    # that is to be displayed.
    MODULE_NAME = "refl_gensim.py"
    PATH_TO_MODULE = inspect.stack()[0][1]
    # Removing name of module from path so that the path only includes up to the
    # directory where the HTML file is located.
    PATH_TO_HTML = PATH_TO_MODULE[:-len(MODULE_NAME)]
    webbrowser.open("file:///" + PATH_TO_HTML + "e/" + vis_html_file_name, new=2)
    logging.info("Gensim visualization has been displayed.")
    return
