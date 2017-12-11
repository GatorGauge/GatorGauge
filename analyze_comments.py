""" analyze java source code comments """


from analyze_java import get_java_strings
from analyze_sentiment import get_avg_sentiment
import parse_comments as pc


def analyze_comments(out):
    """ produce cohesive analysis output regarding comments """
    java_source = get_java_strings(out)

    # accumulator vars
    sum_count_javadoc = 0
    sum_count_multiline = 0
    sum_count_singleline = 0
    sum_ratio_javadoc = 0
    sum_ratio_multiline = 0
    sum_ratio_singleline = 0
    count_tracker = 0

    # accumulate counts and ratios
    for java_string in java_source:
        sum_count_javadoc += pc.count_javadoc_java_comments(java_string)
        sum_count_multiline += pc.count_multiline_java_comments(java_string)
        sum_count_singleline += pc.count_singleline_java_comments(java_string)
        sum_ratio_javadoc += pc.ratio_of_javadoc_comments(java_string)
        sum_ratio_multiline += pc.ratio_of_multiline_comments(java_string)
        sum_ratio_singleline += pc.ratio_of_singleline_comments(java_string)
        count_tracker += 1  # track how many we've summed thus far

    # convert summations to averages
    avg_count_javadoc = sum_count_javadoc / count_tracker
    avg_count_multiline = sum_count_multiline / count_tracker
    avg_count_singleline = sum_count_singleline / count_tracker
    avg_ratio_javadoc = sum_ratio_javadoc / count_tracker
    avg_ratio_multiline = sum_ratio_multiline / count_tracker
    avg_ratio_singleline = sum_ratio_singleline / count_tracker

    # handle sentiment analysis
    (singleline_comments, multiline_comments, javadoc_comments) = \
        pc.get_all_comments(java_source)
    avg_sentiment = get_avg_sentiment(singleline_comments + multiline_comments)

    # FIXME: handle gensim analysis
    gensim_analysis(javadoc_comments)

    # format results for terminal printing
    string_buffer = "\n" + \
        "Singleline Comments\n" + \
        "\tAverage Count: " + avg_count_singleline + \
        "\tAverage Ratio: " + avg_ratio_singleline + \
        "Multiline Comments\n" + \
        "\tAverage Count: " + avg_count_multiline + \
        "\tAverage Ratio: " + avg_ratio_multiline + \
        "JavaDoc Comments\n" + \
        "\tAverage Count: " + avg_count_javadoc + \
        "\tAverage Ratio: " + avg_ratio_javadoc + \
        "Average Sentiment: " + avg_sentiment
    print(string_buffer)  # ... and print them

    # format results for HTML embedding
    html_buffer = "<br>" + \
        "<b>Singleline Comments</b><ul>" + \
        "<li>Average Count: " + avg_count_singleline + "</li>" + \
        "<li>Average Ratio: " + avg_ratio_singleline + "</li>" + \
        "</ul><b>Multiline Comments</b><ul>" + \
        "<li>Average Count: " + avg_count_multiline + "</li>" + \
        "<li>Average Ratio: " + avg_ratio_multiline + "</li>" + \
        "</ul><b>JavaDoc Comments</b><ul>" + \
        "<li>Average Count: " + avg_count_javadoc + "</li>" + \
        "<li>Average Ratio: " + avg_ratio_javadoc + "</li></ul>" + \
        "<b>Average Sentiment</b>: " + avg_sentiment

    # ... and embed them

    # FIXME: append html_buffer to generated LDA html page

    # FIXME: automatically open gensim LDA html page?
