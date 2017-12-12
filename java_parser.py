""" Functions to get statistics about parsed java files. Expects all parameter
inputs to be java source code strings with all spaces, new lines, and comments
removed. Requirement: `pip install javalang` """


import javalang


def get_number_of_variables(java_string):
    """ Counts number of declared variables in java code string using
        javalang library """
    tree = javalang.parse.parse(java_string)
    data = list(tree.filter(javalang.tree.VariableDeclaration))
    num = len(data)
    return num


def get_number_of_methods(java_string):
    """ Counts number of methods in java code string using javalang library """
    tree = javalang.parse.parse(java_string)
    data = list(tree.filter(javalang.tree.MethodDeclaration))
    num = len(data)
    return num


def get_number_of_classes(java_string):
    """ Counts number of defined classes in java code string using
        javalang library """
    tree = javalang.parse.parse(java_string)
    data = list(tree.filter(javalang.tree.ClassDeclaration))
    num = len(data)
    return num


def get_number_of_lines(java_string):
    """ Counts number of lines in java code. We consider any semicolons, open
        brackets, and closed brakets new line starts. Excludes empty lines. """
    num = 0
    for char in java_string:
        if char == ';' or char == '{' or char == '}':
            num += 1
    return num
