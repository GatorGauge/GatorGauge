"""
Functions to get statistics about parsed java files. Expects all parameter inputs
to be java source code strings with all spaces, new lines, and comments removed.
Requirement:
pip install javalang
"""


import javalang


def getNumberOfVariables(javaString):
    """ Counts number of declared variables in java code string using
        javalang library """
    tree = javalang.parse.parse(javaString)
    data = list(tree.filter(javalang.tree.VariableDeclaration))
    num = len(data)
    return num


def getNumberOfMethods(javaString):
    """ Counts number of methods in java code string using javalang library """
    tree = javalang.parse.parse(javaString)
    data = list(tree.filter(javalang.tree.MethodDeclaration))
    num = len(data)
    return num


def getNumberOfClasses(javaString):
    """ Counts number of defined classes in java code string using
        javalang library """
    tree = javalang.parse.parse(javaString)
    data = list(tree.filter(javalang.tree.ClassDeclaration))
    num = len(data)
    return num


def getNumberOfLines(javaString):
    """ Counts number of lines in java code. We consider any semicolons, open
        brackets, and closed brakets new line starts. Excludes empty lines. """
    num = 0
    for c in javaString:
        if c == ';' or c == '{' or c == '}':
            num += 1
    return num
