import file_list
import java_to_string as j
import java_parser as p
import numpy as np
import statistics


def get_java_strings(out):
    java_files = file_list.list_files(".java", out, True)
    repoDict = dict()
    for f in java_files:
        # The second replace is so that code doesn't break on windows
        currFile = f.replace(out,"").replace("\\","/")
        repo = currFile.split("/")[1]
        if repo in repoDict:
            continue
        files = []
        for javaFile in java_files:
            if repo in javaFile:
                files.append(javaFile)
        repoDict[repo] = files

    java_strings = []

    for key, values in repoDict.items():
        java_string = []
        for value in values:
            java_string.append(j.read_and_convert(value))
        java_strings.append(' '.join(java_string))

    return java_strings

def analyze_java(java_strings):
    variableList = []
    methodList= []
    classList = []
    lineList = []
    list_list = dict()
    for java_string in java_strings:
        variableList.append(p.getNumberOfVariables(java_string))
        methodList.append(p.getNumberOfMethods(java_string))
        classList.append(p.getNumberOfClasses(java_string))
        lineList.append(p.getNumberOfLines(java_string))
    list_list["variables"] = variableList
    list_list["methods"] = methodList
    list_list["classes"] = classList
    list_list["lines"] = lineList
    statistics.printStatistics(list_list)
