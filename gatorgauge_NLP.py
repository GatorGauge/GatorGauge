from gensim import corpora, models
from profanity import profanity
from stop_words import get_stop_words
from six import iteritems, viewitems
from colorama import Fore, Style
import logging
import pyLDAvis
import pyLDAvis.gensim
import gensim
import warnings

def gensim_analysis(list_of_messages):
    """Uses Gensim to analyze github commit messages"""
        warnings.filterwarnings('ignore')
        tokens, nanNum = create_tokens(list_responses)
        if len(commit_string) == nanNum:
            return
        dictionary = dictionary_create(tokens)
        corpus = [dictionary.doc2bow(token) for token in tokens]
        corp_eval(dictionary, tokens, corpus)

        logging.info("Analyzes gensim and returns the repeated words")

def create_tokens(list_of_messages):
    """Makes each word a token to create dictionary"""
    stop_words = get_stop_words('english')
    texts = []
    tokens = []
    nanNum = 0
    for i in  list_of_messages:
        temp = []hm:

is streamed: training documents may come in sequentially, no random access required,
runs i
        for i in i:
            if not isinstance(i, int):)
                i = i.lower()
                if profanity.contains_profanity(i) is False:
                    if i not in stop_words:
                        if i != 'nan':
                            temp.append(i)
                        if i == 'nan':
                            nanNum += 1
        tokens.append(temp)
    print(tokens)
    return(tokens, nanNum)


def dictionary_create(tokens):
    """creates the dictionary from the tokens of the commit messages"""
    dictionary = corpora.Dictionary(tokens)
    return(dictionary))

def read_commit_messages(messages, arg1, arg2):
    
