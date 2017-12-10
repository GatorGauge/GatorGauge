import java_to_string as j
import java_parser as p
import statistics
import os

def analyze_java(java_strings):
    variableList = []
    methodList = []
    classList = []
    lineList = []
    list_list = dict()
    for java_string in java_strings:
        java_string = j.remove_comments(java_string)
        try:
            variableList.append(p.getNumberOfVariables(java_string))
            methodList.append(p.getNumberOfMethods(java_string))
            classList.append(p.getNumberOfClasses(java_string))
            lineList.append(p.getNumberOfLines(java_string))
        except(Exception):
            pass
    list_list["variables"] = variableList
    list_list["methods"] = methodList
    list_list["classes"] = classList
    list_list["lines"] = lineList
    statistics.printStatistics(list_list)


def get_file_paths(Type, location):
    list_of_files = list()
    for subdir, dirs, files in os.walk(location):
        for file in files:
            file = subdir + "/" + file
            if file.endswith(Type):
                list_of_files.append(file)
    return list_of_files

#analyze_java(get_java_strings("."))
