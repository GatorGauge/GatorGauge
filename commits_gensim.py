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
                            def read_commit_messages(messages, arg1, arg2):nanNum += 1
        tokens.append(temp)
    print(tokens)
    return(tokens, nanNum)


def dictionary_create(tokens):
    """Creates the dictionary from the tokens of the commit messages"""
    dictionary = corpora.Dictionary(tokens)
    return(dictionary))

<<<<<<< HEAD
def corp_eval(dictionary, tokens, corpus):
    """Evaluate the corpus and produce gensim visualization."""
    i = len(tokens)
    lda = gensim.models.ldamodel.LdaModel(
        corpus,
        id2word=dictionary,
        num_topics=3,
        passes=1,
        alpha='symmetric',
        eta=None)
    corpus = [dictionary.doc2bow(token) for token in tokens]
    logging.debug(dictionary.token2id)
    logging.debug(viewitems(dictionary.dfs))

    print(lda)
    vis = pyLDAvis.gensim.prepare(lda, corpus, dictionary)
    print(Fore.YELLOW + "These are the current topics: " + Style.RESET_ALL)
    print(lda.print_topics(i))
    print(Fore.CYAN +
          "Opening up visualization in a new tab in the browser...",
          Style.RESET_ALL)

    # Writing HTML of visualization to file instead of showing with pyLDAvis show function
    # because the show function starts a server, which allows only one file to be displayed
    # at once.
    vis_html_text = pyLDAvis.prepared_data_to_html(vis)
    vis_html_file_name = "vis" + str(3) + ".html"
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
    webbrowser.open("file:///" + PATH_TO_HTML + vis_html_file_name, new=2)
    logging.info("Gensim visualization has been displayed.")
    return dictionary.dfs
=======
def emoji_intake(emojiData):
    """Creates visual of emojis and emoji topics"""


def read_commit_messages(messages, arg1, arg2):
>>>>>>> 974353696fe8691750f161d849d60121a90d1136
