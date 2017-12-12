""" analyze java source code """

import os
import statistics
import java_to_string as j
import java_parser as p
import write_to_file as wtf


def get_file_paths(filetype, location):
    """ return list of filepaths """
    list_of_files = list()
    for subdir, _dirs, files in os.walk(location):
        for file in files:
            file = subdir + "/" + file
            if file.endswith(filetype):
                list_of_files.append(file)
    return list_of_files


def get_java_strings(out):
    """ return java source code strings """
    java_files = get_file_paths(".java", out)
    repo_dict = dict()
    for file in java_files:
        # The second replace is so that code doesn't break on windows
        curr_file = file.replace(out, "").replace("\\", "/")
        repo = curr_file.split("/")[1]
        if repo in repo_dict:
            continue
        files = []
        for java_file in java_files:
            if repo in java_file:
                files.append(java_file)
        repo_dict[repo] = files
    java_strings = []
    for key, values in repo_dict.items():
        java_string = []
        for value in values:
            java_string.append(j.read_and_convert(value))
        java_strings.append(' '.join(java_string))
    return java_strings


def get_source_code_values(java_strings):
    """ Gets values for variables, methods, classes, and lines in dictionary """
    variable_list = []
    method_list = []
    class_list = []
    line_list = []
    stat_dictionary = dict()
    for java_string in java_strings:
        java_string = j.remove_comments(java_string)
        try:
            variable_list.append(p.get_number_of_variables(java_string))
            method_list.append(p.get_number_of_methods(java_string))
            class_list.append(p.get_number_of_classes(java_string))
            line_list.append(p.get_number_of_lines(java_string))
        except Exception:
            pass
    stat_dictionary["variables"] = variable_list
    stat_dictionary["methods"] = method_list
    stat_dictionary["classes"] = class_list
    stat_dictionary["lines"] = line_list
    return stat_dictionary


def analyze_java(out):
    java_strings = get_java_strings("./"+out)
    stat_dictionary = get_source_code_values(java_strings)
    stat_string = statistics.combine_statistics(stat_dictionary)
    print(stat_string)
    file_name = input("What would you like the file name to be called? ") \
        + ".txt"
    file_name = file_name.replace(" ", "_")
    wtf.write_to_existing_file(stat_string, file_name)
