""" main file in the GatorGauge system """
import sys
import os
# local imports
import github_clone_all
import defaults
import read_file

if __name__ == "__main__":

    defined_commands = {"get", "help", "quit"}
    fSet = frozenset(defined_commands)
    defined_responses = {"Y", "y", "N", "n"}
    rSet = frozenset(defined_responses)

    command = str(input('>>> '))
    while command not in fSet:
        print("Please enter a valid command")
        command = str(input('>>> '))

    while command != "quit":
        token = defaults.TOKEN
        project = defaults.PROJECT
        prefix = defaults.PREFIX
        out = defaults.OUT
        if command == "get":
            if defaults.TOKEN == "":
                token = str(input("GatorGauge requires a GitHub token.  Enter the token for the repo: "))
            if defaults.PROJECT == "":
                project = str(input("Enter the name of the project: "))
            if defaults.PREFIX == "":
                ask_prefix = str(input("Would you like to specify a prefix? (Y/N): "))
                while ask_prefix not in rSet:
                    ask_prefix = str(input("Please enter Y or N: "))
                if ask_prefix == "Y" or ask_prefix == "y":
                    prefix = str(input("Enter the prefix for the repo: "))
                elif ask_prefix == "N" or ask_prefix == "n":
                    prefix = defaults.PREFIX
            if defaults.OUT == "":
                ask_out = str(input("Would you like to specify the destiantion? (Y/N): "))
                while ask_out not in rSet:
                    ask_out = str(input("Please enter Y or N: "))
                if ask_out == "Y" or ask_out == "y":
                    ask_out = str(input("Enter the destination: "))
                elif ask_out == "N" or ask_out == "n":
                    out = defaults.OUT
            github_clone_all.get_repositories(project, prefix, token, out)
        elif command == "help":
            print("help")
        command = str(input('>>> '))
        while command not in fSet:
            print("Please enter a valid command")
            command = str(input('>>> '))
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
        github_clone_all.get_repositories(args.project, args.prefix, args.token, args.out)

    # read inputed file
    if args.read is not "":
        listFiles = list()
        for subdir, dirs, files in os.walk(args.out):
            for file in files:
                if file.endswith(args.read):
                    listFiles.append(os.path.join(subdir, file))
        for File in listFiles:
            print(*read_file.read_file(File),end="\n\n")

    if "--list" in sys.argv[1:]: # checks if --list was used in command line
        files = file_list.list_files(args.list, args.out) # list of files returned
        for file in files:
            print(file)
