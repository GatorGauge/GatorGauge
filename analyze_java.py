import file_list
import java_to_string
import java_parser as p
import numpy


def getStatistics(listVar, listMeth, listClass, listLine):
    print("Average number of variables: ", numpy.mean(listVar))
    print("Average number of methods: ", numpy.mean(listMeth))
    print("Average number of classes: ",numpy.mean(listClass))
    print("Average number of lines: ", numpy.mean(listLine))

    print("Standard deviation of variables: ", numpy.std(listVar))
    print("Standard deviation of methods: ", numpy.std(listMeth))
    print("Standard deviation of classes: ", numpy.std(listClass))
    print("Standard deviation of lines: ", numpy.std(listLine))


def collectByRepo(javaFiles,out):
    repoDict = dict()
    for f in javaFiles:
        currFile = f.replace(out,"").replace("\\","/")
        repo = currFile.split("/")[1]
        if repo in repoDict:
            continue
        files = []
        for javaFile in javaFiles:
            if repo in javaFile:
                files.append(javaFile)
        repoDict[repo] = files

    print(repoDict)
    return repoDict

def analyze_java(out):
    variableList = []
    methodList= []
    classList = []
    lineList = []

    print("Analyzing java files:")
    java_files = file_list.list_files(".java", out, True)
    dictionary = collectByRepo(java_files,out)

    for username, files in dictionary.items():
        v = m = c = l = 0
        ignore = False
        for java_file in files:
            java_string = java_to_string.read_and_convert(java_file)
            java_string = java_to_string.remove_comments(java_string)[:]
            try:
                v = v + p.getNumberOfVariables(java_string)
                m = m + p.getNumberOfMethods(java_string)
                c = c + p.getNumberOfClasses(java_string)
                l = l + p.getNumberOfLines(java_string)
            except(Exception):
                ignore = True
                break
        if not ignore:
            variableList.append(v)
            methodList.append(m)
            classList.append(c)
            lineList.append(l)

    getStatistics(variableList, methodList, classList, lineList)
