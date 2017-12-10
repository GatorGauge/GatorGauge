""" list all of the repositories in Out or all of the files in a given repository """
import os


def list_files(repo, out):
    repo_list = list()  # list of file names to return
    if repo is not "all" and not os.path.isdir(
            "./" + str(out) + "/" + str(repo)):  # check if file location exists
        print(
            "\tERROR: Repository: '" +
            str(repo) +
            "' does not exists")
        return
    if repo is "all":
        # list of all directories inside of Out folder
        for subdir, dirs, files in os.walk("./" + str(out)):
            repo_list = dirs
            break
    else:
        for subdir, dirs, files in os.walk("./" + str(out) + "/" + str(repo)):
            for file in files:
                if "." in file:  # ignore files with no '.' extension
                    if file not in repo_list:  # get each unique file name
                        repo_list.append(file)
    return repo_list
