""" read java source code files and convert to strings """

import re


def read_and_convert(java_file):
    """The read_and_convert function reads in a Java File
    and returns the source code from the file, including comments"""
    with open(java_file, 'r') as src:
        source_code = src.read()

    return source_code


def remove_comments(java_string):
    """The remove_comments function removes all comments
    from the Java source code returned by read_and_convert.
    This function outputs the entire source code as a string
    with zero whitespaces"""
    # remove multiline comments of the form (/* comment */)
    java_string = re.sub(
        re.compile(r"(?<=/\*).*?(?=\*/)", re.DOTALL), "", java_string)
    # remove all single line comments
    java_string = re.sub(re.compile("//.*?\n"), "", java_string)
    # replace a new line with a blank character
    java_string = java_string.replace("\n", "")
    java_string = java_string.replace("/**/", "")  # remove comment residue
    return java_string
