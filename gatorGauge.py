""" main file in the GatorGauge system """
#import sys
import os
# local imports
import github_clone_all
import defaults
import get_reflection
import file_list
import display

if __name__ == "__main__":

    print("Welcome to GatorGauge!")
    print("Type help to see list of commands.")

    defined_commands = {"help", "get", "config", "list", "analyze", "quit"}
    fSet = frozenset(defined_commands)
    defined_responses = {"Y", "y", "N", "n"}
    rSet = frozenset(defined_responses)

    command = str(input('>>> '))
    args = []
    # added 2 more args for taking in project, prefix, token,
    arg1 = ""
    arg2 = ""
    fileName = ""
    token = defaults.TOKEN
    project = defaults.PROJECT
    keywords = defaults.KEYWORDS
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
        if command == "get":
            if token is "" or project is "":
                token, project, keywords, out = defaults.editConfig()
            ask_prefix = str(
                input(
                    "Download all repositories in " +
                    project +
                    " that have " +
                    keywords +
                    " in their name and place in directory '" +
                    out + "' with token: " + token +
                    "' (Y/N): "))
            if ask_prefix == "Y" or ask_prefix == "y":
                github_clone_all.get_repositories(project, keywords, token, out)
            token = defaults.TOKEN
            project = defaults.PROJECT
            keywords = defaults.KEYWORDS
            out = defaults.OUT
        # allow edit of config file from program
        elif command == "config":
            # reset values with inputted values
            token, project, prefix, out = defaults.editConfig()
        elif command == "list":
            rep = "all"
            if arg1 is not "":
                rep = arg1
            repo = file_list.list_files(rep)  # list of files returned
            for r in repo:
                print(r)
        elif command == "analyze":
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
                print(read_file.read_file(File), end="\n\n")
        elif command == "help":
            if arg1 == "":
                print(display.display_help())
            else:
                print(display.display_help_with_command(arg1))
        command = str(input('>>> '))
        arg1 = ""
        arg2 = ""
