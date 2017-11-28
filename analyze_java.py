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
def analyze_java(out):
    variableList = []
    methodList= []
    classList = []
    lineList = []
    print("Analyzing java files:")
    java_files = file_list.list_files("java", out, True)
    for java_file in java_files:
        java_string = java_to_string.read_and_convert(java_file)
        java_string = java_to_string.remove_comments(java_string)[:]
        try:
            print (java_file)
            variableList.append(p.getNumberOfVariables(java_string))
            methodList.append(p.getNumberOfMethods(java_string))
            classList.append(p.getNumberOfClasses(java_string))
            lineList.append(p.getNumberOfLines(java_string))
        except(Exception):
            print ("error")
    #print(variables)
    #print(methods)
    #print(classes)
    #print(lines)
    getStatistics(variableList, methodList, classList, lineList)
