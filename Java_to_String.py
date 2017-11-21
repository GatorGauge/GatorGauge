# Importing regex library
import re
import java_parser


def read_and_convert(javaFile):
    """The read_and_convert function reads in a Java File
    and returns the source code from the file, including comments"""
    with open(javaFile, 'r') as src:
        source_code = src.read()

    return source_code


def remove_comments(javaString):
    """The remove_comments function removes all comments
    from the Java source code returned by read_and_convert.
    This function outputs the entire source code as a string
    with zero whitespaces"""
    javaString = re.sub(re.compile("(?<=/\*).*?(?=\*/)",re.DOTALL ) ,"" ,javaString) # remove multiline comments of the form (/* comment */)
    javaString = re.sub(re.compile("//.*?\n" ) ,"" ,javaString) # remove all single line comments
    javaString = javaString.replace("\n", "") # replace a new line with a blank character
    javaString = javaString.replace("/**/","") # remove comment residue
    return javaString


# Test code for demonstration
data = read_and_convert("TipCalculator.java")
newData = remove_comments(data)

print("Number of lines = "+str(java_parser.getNumberOfLines(newData)))
print("Number of variables = "+str(java_parser.getNumberOfVariables(newData)))
print("Number of methods = "+str(java_parser.getNumberOfMethods(newData)))
print("Number of classes = "+str(java_parser.getNumberOfClasses(newData)))
