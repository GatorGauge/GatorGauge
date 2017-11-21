# Importing regex library
import re


def read_and_convert(JavaFile):
    """The read_and_convert function reads in a Java File
    and returns the source code from the file, including comments"""
    with open(JavaFile, 'r') as src:
        source_code = src.read()

    return source_code



def remove_comments(string):
    """The remove_comments function removes all comments
    from the Java source code returned by read_and_convert.
    This function outputs the entire source code as a string
    with zero whitespaces"""
    string = re.sub(re.compile("/\*.*?\*/",re.DOTALL ) ,"" ,string) # remove multiline comments of the form (/* comment */)
    string = re.sub(re.compile("//.*?\n" ) ,"" ,string) # remove all single line comments
    string = string.replace("\n", "") # replace a new line with a blank character
    string = string.replace(" ", "") # replace all whitespaces with a blank character
    print(string)
    return string

# Function calls
data = read_and_convert("TipCalculator.java")
remove_comments(data)