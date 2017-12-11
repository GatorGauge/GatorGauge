""" analyze java source code """

import os
import statistics
import java_to_string as j
import java_parser as p


<<<<<<< HEAD
=======
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
    for _, values in repo_dict.items():
        java_string = []
        for value in values:
            java_string.append(j.read_and_convert(value))
        java_strings.append(' '.join(java_string))
    return java_strings


>>>>>>> origin/master
def analyze_java(java_strings):
    """ analyze java source code strings """
    variable_list = []
    method_list = []
    class_list = []
    line_list = []
    list_list = dict()
    for java_string in java_strings:
        java_string = j.remove_comments(java_string)
        try:
            variable_list.append(p.get_number_of_variables(java_string))
            method_list.append(p.get_number_of_methods(java_string))
            class_list.append(p.get_number_of_classes(java_string))
            line_list.append(p.get_number_of_lines(java_string))
        except Exception:
            pass
    list_list["variables"] = variable_list
    list_list["methods"] = method_list
    list_list["classes"] = class_list
    list_list["lines"] = line_list
    statistics.print_statistics(list_list)


def get_file_paths(filetype, location):
    """ return list of filepaths """
    list_of_files = list()
    for subdir, _dirs, files in os.walk(location):
        for file in files:
            file = subdir + "/" + file
            if file.endswith(filetype):
                list_of_files.append(file)
    return list_of_files

<<<<<<< HEAD
=======

>>>>>>> origin/master
# analyze_java(get_java_strings("."))
