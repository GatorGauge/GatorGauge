""" main file in the GatorGauge system """
import sys
import os
# local imports
import github_clone_all
import parse_args
import defaults
import read_file
import file_list

if __name__ == "__main__":
    ARGS = parse_args.parse_args(sys.argv[1:])
    # checks if the required information is entered
    if ARGS.token == "" \
            and defaults.TOKEN == "" \
            and ARGS.get is True \
            and defaults.PROJECT == "" \
            and ARGS.project == "":
        print("\tERROR: A Github token is required for the system to run." +
              " Please enter one in either config.ini or in the command line" +
              " with the --token flag")
        print("\tERROR: '--get' requires either a default project name " +
              "(in config.ini) or a supplied '--project' flag")
        quit()
    elif ARGS.token == "" and defaults.TOKEN == "":
        print("\tERROR: A Github token is required for the system to run." +
              " Please enter one in either config.ini or in the command line" +
              " with the --token flag")
        quit()
    elif ARGS.get is True and defaults.PROJECT == "" and ARGS.project == "":
        print("\tERROR: '--get' requires either a default project name" +
              " in config.ini or supplied with the '--project' flag")
        quit()

    # download repositories
    if ARGS.get is True:
        github_clone_all.get_repositories(
            ARGS.project, ARGS.prefix, ARGS.token, ARGS.out)
    # read inputed file
    if ARGS.read:
        LIST_OF_FILES = list()
        for subdir, dirs, files in os.walk(ARGS.out):
            for file in files:
                if file.endswith(ARGS.read):
                    LIST_OF_FILES.append(os.path.join(subdir, file))
        for File in LIST_OF_FILES:
            print(*read_file.read_file(File), end="\n\n")

    if "--list" in sys.argv[1:]:  # checks if --list was used in command line
        FILES = file_list.list_files(
            ARGS.list, ARGS.out)  # list of files returned
        for file in FILES:
            print(file)
