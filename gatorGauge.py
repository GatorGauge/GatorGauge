""" main file in the GatorGauge system """
#import sys
import os
# local imports
import github_clone_all
import defaults
import read_file
import file_list
import display

if __name__ == "__main__":

    print("Welcome to GatorGauge!")
    print("Type help to see list of commands.")

    defined_commands = {"help", "get", "config", "list", "read", "gensim", "quit"}
    fSet = frozenset(defined_commands)
    defined_responses = {"Y", "y", "N", "n"}
    rSet = frozenset(defined_responses)

    command = str(input('>>> '))
    args = []
    # added 2 more args for taking in project, prefix, token,
    arg1 = ""
    arg2 = ""
    arg3 = ""
    fileName = ""
    token = defaults.TOKEN
    project = defaults.PROJECT
    prefix = defaults.PREFIX
    out = defaults.OUT
    while command != "quit":
        args = command.rsplit()
        command = args[0]
        while args[0] not in fSet:
            print("Please enter a valid command")
            command = str(input('>>> '))
            args = command.rsplit()
            command = args[0]
        if len(args) == 2:
            arg1 = args[1]
        elif len(args) == 3:
            arg1 = args[1]
            arg2 = args[2]
        elif len(args) == 4:
            arg1 = args[1]
            arg2 = args[2]
            arg3 = args[3]
        elif len(args) == 5:
            arg1 = args[1]
            arg2 = args[2]
            arg3 = args[3]
            arg4 = args[4]
        if command == "get":
            if token == "":
                token = str(
                    input("GatorGauge requires a GitHub token.  Enter the token for the repo: "))
            if project == "":
                project = str(input("Enter the name of the project: "))
            if prefix == "":
                ask_prefix = str(
                    input("Would you like to specify a prefix? (Y/N): "))
                while ask_prefix not in rSet:
                    ask_prefix = str(input("Please enter Y or N: "))
                if ask_prefix == "Y" or ask_prefix == "y":
                    prefix = str(input("Enter the prefix for the repo: "))
                elif ask_prefix == "N" or ask_prefix == "n":
                    prefix = defaults.PREFIX
            if out == "":
                ask_out = str(
                    input("Would you like to specify the destiantion? (Y/N): "))
                while ask_out not in rSet:
                    ask_out = str(input("Please enter Y or N: "))
                if ask_out == "Y" or ask_out == "y":
                    ask_out = str(input("Enter the destination: "))
                elif ask_out == "N" or ask_out == "n":
                    out = defaults.OUT
            ask_prefix = str(
                input(
                    "Download all repositories in " +
                    project +
                    " that have " +
                    prefix +
                    " in their name and place in directory '" +
                    out + "' with token: " + token +
                    "' (Y/N): "))
            if ask_prefix == "Y" or ask_prefix == "y":
                github_clone_all.get_repositories(project, prefix, token, out)
            token = defaults.TOKEN
            project = defaults.PROJECT
            prefix = defaults.PREFIX
            out = defaults.OUT
        # allow edit of config file from program
        elif command == "config":
            # reset values with inputted values
            token, project, prefix, out = defaults.editConfig()
        elif command == "list":
            if arg1 is "":
                fileType = "all"
            elif not "." in arg1 and arg1 is not "":
                out = arg1
                fileType = "all"
            elif arg2 is not None and arg1 is not "":
                fileType = arg1
                out = arg2
            files = file_list.list_files(fileType, out)  # list of files returned
            if len(files) is 0:
                print("ERROR: File '" + str(arg1) + "' does not exist")
            for file in files:
                print(file)
        elif command == "read":
            while arg1 == "":
                print("You must enter a file name or type.")
                arg1 = str(input('File name or type: '))
            if arg2 != "":
                out = arg2
            listFiles = list()
            for subdir, dirs, files in os.walk("./" + str(out)):
                for file in files:
                    if file.endswith(arg1):
                        listFiles.append(os.path.join(subdir, file))
            if len(listFiles) == 0:
                print("ERROR: File '" + str(arg1) + "' does not exist")
            for File in listFiles:
                print(*read_file.read_file(File), end="\n\n")
            fileName = arg1
        elif command == "help":
            if arg1 == "":
                print(display.display_help())
            else:
                print(display.display_help_with_command(arg1))
        command = str(input('>>> '))
        arg1 = ""
        arg2 = ""
        arg3 = ""
# Error messages from old version of gatorGauge
#    args = parse_args.parse_args(sys.argv[1:])
#    # checks if the required information is entered
#    if args.token == "" and defaults.TOKEN == "" and args.get is True and defaults.PROJECT == "" and args.project == "":
#        print("\tERROR: A Github token is required for the system to run. Please enter one in either config.ini or in the command line with the --token flag")
#        print("\tERROR: '--get' requires either a default project name (in config.ini) or a supplied '--project' flag")
#        quit()
#    elif args.token == "" and defaults.TOKEN == "":
#        print("\tERROR: A Github token is required for the system to run. Please enter one in either config.ini or in the command line with the --token flag")
#        quit()
#    elif args.get is True and defaults.PROJECT == "" and args.project == "":
#        print("\tERROR: '--get' requires either a default project name in config.ini or supplied with the '--project' flag")
#        quit()
