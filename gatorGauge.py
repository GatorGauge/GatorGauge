""" main file in the GatorGauge system """
import sys
import os
# local imports
import github_clone_all
import parse_args
import defaults
import read_file

if __name__ == "__main__":
    args = parse_args.parse_args(sys.argv[1:])
    # checks if the required information is entered
    if args.token == "" and defaults.TOKEN == "" and args.get is True and defaults.PROJECT == "" and args.project == "":
        print("\tERROR: A Github token is required for the system to run. Please enter one in either config.ini or in the command line with the --token flag")
        print("\tERROR: '--get' requires either a default project name (in config.ini) or a supplied '--project' flag")
        quit()
    elif args.token == "" and defaults.TOKEN == "":
        print("\tERROR: A Github token is required for the system to run. Please enter one in either config.ini or in the command line with the --token flag")
        quit()
    elif args.get is True and defaults.PROJECT == "" and args.project == "":
        print("\tERROR: '--get' requires either a default project name in config.ini or supplied with the '--project' flag")
        quit()

    # download repositories
    if args.get is True:
        github_clone_all.get_repositories(
            args.project, args.prefix, args.token, args.out)
    # read inputed file
    if args.read is not "":
        listFiles = list()
        for subdir, dirs, files in os.walk(args.out):
            for file in files:
                if file.endswith(args.read):
                    listFiles.append(os.path.join(subdir, file))
        for File in listFiles:
            print(*read_file.read_file(File), end="\n\n")
