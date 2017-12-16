""" main file in the GatorGauge system """
import sys
import os

# local imports
import github_clone_all
import defaults
import file_list
import display
import parse_args
import analyze_commits
import analyze_java
import analyze_comments
import analyze_reflection


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
    PROJECT = defaults.get_project()
    KEYWORDS = str(defaults.get_keywords()).split(',')
    OUT = defaults.get_out()
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
                PROJECT = defaults.edit_config_project()
                #KEYWORDS, OUT = defaults.edit_config()
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
                PROJECT = defaults.edit_config_project()
                KEYWORDS = defaults.edit_config_keywords()
                OUT = defaults.edit_config_directory()
                defaults.save_config_changes(PROJECT, KEYWORDS, OUT)
                KEYWORDS = KEYWORDS.split(',')
            elif ARG1 == "refresh":
                print("Config values refreshed")
                PROJECT = defaults.get_project()
                KEYWORDS = str(defaults.get_keywords()).split(',')
                OUT = defaults.get_out()
            else:
                print("Project: " + str(PROJECT))
                print("Keywords: " + str(KEYWORDS))
                print("Out: " + str(OUT))
        elif COMMAND == "list":
            if ARG1:
                REP = ARG1
            else:
                REP = "all"
            # list of repositories or files in specified repository returned
            REPO = file_list.list_files(REP, OUT)
            for r in REPO:
                print(r)
        elif COMMAND == "analyze":
            while ARG1 not in SPECIFIERS:
                print("You must enter a specifier " + str(SPECIFIERS) + ".")
                ARG1 = str(input('Specifier: '))
            if ARG1 == "source":
                analyze_java.analyze_java(OUT)
            elif ARG1 == "comments":
                analyze_comments.analyze_comments(OUT)
            elif ARG1 == "commits":
                analyze_commits.analyze_commits(OUT)
            elif ARG1 == "reflection":
                analyze_reflection.analyze_reflection(OUT)
        elif COMMAND == "help":
            if ARG1 == "":
                print(display.display_help())
            else:
                print(display.display_help_with_command(ARG1))
        COMMAND = str(input('>>> '))
        ARG1 = ""
        ARG2 = ""
