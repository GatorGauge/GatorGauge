""" main file in the GatorGauge system """

import sys
import os

import github_clone_all
import defaults
import get_reflection
import file_list
import display
import parse_args


if __name__ == "__main__":
    print("Welcome to GatorGauge!")
    print("Type help to see list of commands.")
    ARGS = parse_args.parse_args(sys.argv[1:])
    TOKEN = ARGS.token
    while TOKEN == "":
        TOKEN = str(input("Please enter a valid token: "))
    # if there is no config.ini file, create one
    if not os.path.exists("./config.ini"):
        defaults.new_config()
        defaults.edit_config()
    DEFINED_COMMANDS = {"help", "get", "config", "list", "analyze", "quit"}
    FSET = frozenset(DEFINED_COMMANDS)
    SPECIFIERS = ('source', 'comments', 'commits', 'reflection')

    COMMAND = str(input('>>> '))
    ARGS = []
    # added 2 more args for taking in project, prefix, token,
    ARG1 = ""
    ARG2 = ""
    FILENAME = ""
    PROJECT = defaults.PROJECT
    KEYWORDS = str(defaults.KEYWORDS).split(',')
    OUT = defaults.OUT
    while COMMAND != "quit":
        ARGS = COMMAND.rsplit()
        COMMAND = ARGS[0]
        while ARGS[0] not in FSET:
            print("Please enter a valid command")
            COMMAND = str(input('>>> '))
            ARGS = COMMAND.rsplit()
            COMMAND = ARGS[0]
            if COMMAND == "quit":
                quit()
        if len(ARGS) == 2:
            ARG1 = ARGS[1]
        elif len(ARGS) == 3:
            ARG1 = ARGS[1]
            ARG2 = ARGS[2]
        if COMMAND == "get":
            while PROJECT is "":
                PROJECT, KEYWORDS, OUT = defaults.edit_config()
            ASK_PREFIX = str(
                input(
                    "Download all repositories in " +
                    PROJECT +
                    " that have " +
                    str(KEYWORDS) +
                    " in their name and place in directory '" +
                    OUT + "' (Y/N): "))
            if ASK_PREFIX == "Y" or ASK_PREFIX == "y":
                github_clone_all.get_repositories(
                    TOKEN, PROJECT, KEYWORDS, OUT)
        # allows user to edit the config file from program
        elif COMMAND == "config":
            # reset values with inputted values
            if ARG1 == "edit":
                PROJECT, KEYWORDS, OUT = defaults.edit_config()
            elif ARG1 == "reset":
                print("Config values reset")
                PROJECT = defaults.PROJECT
                KEYWORDS = str(defaults.KEYWORDS).split(',')
                OUT = defaults.OUT
            else:
                print("Project: " + str(PROJECT))
                print("Keywords: " + str(KEYWORDS))
                print("Out: " + str(OUT))
        elif COMMAND == "list":
            REP = "all"
            if ARG1:
                REP = ARG1
            # list of repositories or files in specified repository returned
            REPO = file_list.list_files(REP, OUT)
            for r in REPO:
                print(r)
        elif COMMAND == "analyze":
            while ARG1 not in SPECIFIERS:
                print("You must enter a specifier " + str(SPECIFIERS) + ".")
                ARG1 = str(input('Specifier: '))
            if ARG1 == "source":
                print("SOURCE")
            elif ARG1 == "comments":
                print("COMMENTS")
            elif ARG1 == "commits":
                print("COMMITS")
            elif ARG1 == "reflection":
                LISTFILES = list()
                for subdir, dirs, files in os.walk("./" + str(OUT)):
                    for file in files:
                        if file.endswith("reflection.md"):
                            LISTFILES.append(os.path.join(subdir, file))
                if not LISTFILES:
                    print("ERROR: File 'reflection.md' does not exist")
                RESPONSES = list()
                for file in LISTFILES:
                    response = get_reflection.get_reflection(file)
                    RESPONSES.append(response)
                for res in RESPONSES:
                    print(res)
        elif COMMAND == "help":
            if ARG1 == "":
                print(display.display_help())
            else:
                print(display.display_help_with_command(ARG1))
        COMMAND = str(input('>>> '))
        ARG1 = ""
        ARG2 = ""
