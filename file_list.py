""" list all of the files in the location or specified file type """
import os

from defaults import OUT
# Type is the file type (.java, .md, etc), location: where to look at


def list_files(repo):
    repo_list = list()  # list of file names to return
    if repo is not "all" and not os.path.isdir(
            "./" + str(OUT) + "/" + str(repo)):  # check if file location exists
        print(
            "\tERROR: Repository: '" +
            str(repo) +
            "' does not exists")
        return
    if repo is "all":
        # list of all directories inside of Out folder
        repo_list = os.listdir("./" + str(OUT))
    else:
        for subdir, dirs, files in os.walk("./" + str(OUT) + "/" + str(repo)):
            for file in files:
                if "." in file:  # ignore files with no '.' extension
                    if file not in repo_list:  # get each unique file name
                        repo_list.append(file)
    return repo_list
