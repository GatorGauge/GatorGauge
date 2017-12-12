""" analyze java source code comments """


from analyze_java import get_java_strings
from analyze_sentiment import get_avg_sentiment
from gg_gensim import gensim_analysis
from defaults import GENSIM_HTML_OUT
import parse_comments as pc


def calculate_averages(java_source):
    """ calculate average comment counts and ratios """

    # accumulator vars
    sum_ratio_javadoc = 0
    sum_ratio_multiline = 0
    sum_ratio_singleline = 0
    count_tracker = 0

    # accumulate counts and ratios
    for java_string in java_source:
        ratios = pc.get_ratios_of_comments(java_string)
        sum_ratio_javadoc += ratios["javadoc"]
        sum_ratio_multiline += ratios["multiline"]
        sum_ratio_singleline += ratios["singleline"]
        count_tracker += 1  # track how many we've summed thus far

    # convert summations to averages
    avg_ratio_javadoc = sum_ratio_javadoc / count_tracker
    avg_ratio_multiline = sum_ratio_multiline / count_tracker
    avg_ratio_singleline = sum_ratio_singleline / count_tracker
    avg_counts = pc.get_avg_nums_of_comments(java_source)

    return (
        avg_counts["javadoc"],
        avg_counts["multiline"],
        avg_counts["singleline"],
        avg_ratio_javadoc,
        avg_ratio_multiline,
        avg_ratio_singleline)


def analyze_comments(out):
    """ produce cohesive analysis output regarding comments """
    java_source = get_java_strings(out)
    print(java_source)
    # calculate averages
    (avg_count_javadoc,
     avg_count_multiline,
     avg_count_singleline,
     avg_ratio_javadoc,
     avg_ratio_multiline,
     avg_ratio_singleline) = \
        calculate_averages(java_source)

    # handle sentiment analysis
    (singleline, multiline, javadoc) = pc.get_all_comments(java_source)
    avg_sentiment = get_avg_sentiment(singleline + multiline)

<<<<<<< HEAD
    # FIXME: handle gensim analysis
    #gensim_analysis(javadoc)

=======
>>>>>>> origin/master
    # format results for terminal printing
    string_buffer = "\n" + \
        "Singleline Comments\n" + \
        "\tAverage Count: " + str(avg_count_singleline) + \
        "\tAverage Ratio: " + str(avg_ratio_singleline) + \
        "Multiline Comments\n" + \
        "\tAverage Count: " + str(avg_count_multiline) + \
        "\tAverage Ratio: " + str(avg_ratio_multiline) + \
        "JavaDoc Comments\n" + \
        "\tAverage Count: " + str(avg_count_javadoc) + \
        "\tAverage Ratio: " + str(avg_ratio_javadoc) + \
        "Average Sentiment: " + str(avg_sentiment)
    print(string_buffer)  # ... and print them

    # format results for HTML embedding
    html_buffer = "<br>" + \
        "<b>Singleline Comments</b><ul>" + \
        "<li>Average Count: " + str(avg_count_singleline) + "</li>" + \
        "<li>Average Ratio: " + str(avg_ratio_singleline) + "</li>" + \
        "</ul><b>Multiline Comments</b><ul>" + \
        "<li>Average Count: " + str(avg_count_multiline) + "</li>" + \
        "<li>Average Ratio: " + str(avg_ratio_multiline) + "</li>" + \
        "</ul><b>JavaDoc Comments</b><ul>" + \
        "<li>Average Count: " + str(avg_count_javadoc) + "</li>" + \
        "<li>Average Ratio: " + str(avg_ratio_javadoc) + "</li></ul>" + \
        "<b>Average Sentiment</b>: " + str(avg_sentiment)

    # ... and embed them
    embed_stats_into_html(html_buffer)

    # handle gensim analysis
    gensim_analysis(javadoc)


def embed_stats_into_html(stats):
    """ embed the statistics html """
    # warning: this has to happen before gensim adds to the file, if the stats
    # portion is to be visible when the file is opened automatically by gensim.
    file = open(GENSIM_HTML_OUT, "w")
    file.write(stats)
    file.close()
