import file_list
import java_to_string
import java_parser as p

def analyze_java(out):
    print("Analyzing java files:")
    java_files = file_list.list_files("java", out, True)
    for java_file in java_files:
        java_string = java_to_string.read_and_convert(java_file)
        java_string = java_to_string.remove_comments(java_string)[:]
        try:
            print (java_file)
            print ("Number of variables: ", p.getNumberOfVariables(java_string))
            print ("Number of methods: ", p.getNumberOfMethods(java_string))
            print ("Number of classes: ", p.getNumberOfClasses(java_string))
            print ("Number of lines: ", p.getNumberOfLines(java_string))
        except(Exception):
            print ("error")
