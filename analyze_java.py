""" analyze java source code """

import os
import statistics
import java_to_string as j
import java_parser as p
import write_to_file as wtf


def get_file_paths(filetype, location):
    """ return list of filepaths """
    list_of_files = list()
    for subdir, _dirs, files in os.walk(location): # generates files names by walking the tree
        for file in files:
            file = subdir + "/" + file
            if file.endswith(filetype): # checks to see if the file is a java files
                list_of_files.append(file) # adds file to list_of_files
    return list_of_files # returns list of appropriate files


def get_java_strings(out):
    """ return java source code strings """
    java_files = get_file_paths(".java", out) # calls the get_file_paths function for java files in the out folder
    repo_dict = dict() # creation of dictionary data structure
    for file in java_files:
        # The second replace is so that code doesn't break on windows
        curr_file = file.replace(out, "").replace("\\", "/")
        repo = curr_file.split("/")[1] # gives the name of the respository
        if repo in repo_dict:
            continue
        files = []
        for java_file in java_files:
            if repo in java_file:
                files.append(java_file)
        repo_dict[repo] = files # adds to the dictionary name of the file and the filepath
    java_strings = []
    for key, values in repo_dict.items():#
        java_string = []
        for value in values:
            java_string.append(j.read_and_convert(value))# convert file path to a string
        java_strings.append(' '.join(java_string))
    return java_strings # return java strings


def get_source_code_values(java_strings):
    """ Gets values for variables, methods, classes, and lines in dictionary """
    variable_list = []
    method_list = []
    class_list = []
    line_list = []
    stat_dictionary = dict() # creates a dictionary
    for java_string in java_strings:
        java_string = j.remove_comments(java_string)# removes comments from java string
        try:
            variable_list.append(p.get_number_of_variables(java_string)) # gets number of variables and appends it to list
            method_list.append(p.get_number_of_methods(java_string))# gets number of methods and appends it to list
            class_list.append(p.get_number_of_classes(java_string))# gets number of classes and appends it to list
            line_list.append(p.get_number_of_lines(java_string))# gets number of lines and appends it to list
        except Exception:
            pass
    stat_dictionary["variables"] = variable_list # sets variables in the dictionary equal to line_list
    stat_dictionary["methods"] = method_list # sets methods in the dictionary equal to line_list
    stat_dictionary["classes"] = class_list # sets classes in the dictionary equal to line_list
    stat_dictionary["lines"] = line_list # sets lines in the dictionary equal to line_list
    return stat_dictionary


def analyze_java(out):
    if out.endswith('/'): #checks to see that the out function ends with /
        out = out[:len(out) - 1]
    java_strings = get_java_strings(out) # gets java source code strings
    stat_dictionary = get_source_code_values(java_strings) # gets the actual values of java source code
    stat_string = statistics.combine_statistics(stat_dictionary) #gets statistics of the java files
    print(stat_string) # prints statistics neatly
    answer = input("Would you like to save these results to a file? (y/n) ") # allow the option to save results to a file
    if answer.lower() == 'y':
        fileName = input("What would you like the file name to be called? ") \
            + ".txt" # allow the user to supply a file name
        fileName = fileName.replace(" ", "_") # replace spaces with underscores
        wtf.write_to_existing_file(stat_string, fileName) # write to the file
