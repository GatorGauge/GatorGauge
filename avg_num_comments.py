import parse_comments

def printAvg():
    singleLine = parse_comments.count_singleline_java_comments
    multiLine = parse_comments.count_multiline_java_comments
    javadoc = parse_comments.count_javadoc_java_comments
    lineDict = {'single line: ', 'multi-line: ', 'javadoc: '}

    lineDict['single line: '] = singleline
    lineDict['multi-line: '] = multiLine
    lineDict['javadoc: '] = javadoc_comments

    print(lineDict)
    return lineDict
