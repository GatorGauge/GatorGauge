""" list all of the files in the location or specified file type """
import os


def list_files(Type, location):  # Type: file type (.java, .md, etc), location: where to look at
    file_list = list()  # list of file names to return
    if not os.path.isdir(
            "./" + str(location)):  # check if file location exists
        print(
            "\tERROR: File location: '" +
            str(location) +
            "' does not exists")
        quit()
    if Type is 'all':  # if no input for type show all files
        for subdir, dirs, files in os.walk(location):
            for file in files:
                if "." in file:  # ignore files with no . extension
                    if file not in file_list:  # get each unique file name
                        file_list.append(file)
    else:  # show list of files of type Type
        for subdir, dirs, files in os.walk(location):
            for file in files:
                if file.endswith(Type):  # get only files of type Type
                    if file not in file_list:  # get each unique file name
                        file_list.append(file)
    return file_list
