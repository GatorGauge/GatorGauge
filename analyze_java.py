import file_list
import java_to_string as j
import java_parser as p
import numpy as np
import statistics

def getStatistics(numericalList):
    q75, q25 = np.percentile(numericalList, [75,25])
    iqr = q75 - q25
    statString = "min: " + str(np.min(numericalList)) + " max: " \
        + str(np.max(numericalList)) + " mean: " + str(np.mean(numericalList)) \
        + " StdDev: " + str(np.std(numericalList)) + " iqr: " + str(iqr)
    return statString


def get_java_strings(out):
    java_files = file_list.list_files(".java", out, True)
    print(java_files)
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
    list_list = []
    for java_string in java_strings:
        variableList.append(p.getNumberOfVariables(java_string))
        methodList.append(p.getNumberOfMethods(java_string))
        classList.append(p.getNumberOfClasses(java_string))
        lineList.append(p.getNumberOfLines(java_string))
    list_list.append(variableList)
    list_list.append(methodList)
    list_list.append(classList)
    list_list.append(lineList)
    statistics.printStatistics(list_list)
