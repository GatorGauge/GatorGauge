import parse_comments


def get_avg_num_of_comments(java_strings):

    singleLineComments = parse_comments.count_singleline_java_comments(java_strings)
    multiLineComments = parse_comments.count_multiline_java_comments(java_strings)
    javadocComments = parse_comments.count_javadoc_java_comments(java_strings)
    totalLine = parse_comments.get_all_comments(java_strings)

    singleLineComments = singleLine/totalLine
    multiLineComments = multiLine/totalLine
    javadocComments = javadoc/totalLine

    lineDict = {"singleline":singleLineComments, "multiline":multiLineComments, "javadoc":javadocComments}

    for key,val in lineDict.items():
        print(key, "=>", val)

    print(lineDict)
    return lineDict
