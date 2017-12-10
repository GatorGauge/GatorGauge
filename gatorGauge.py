""" main file in the GatorGauge system """
import sys
import os
# local imports
import github_clone_all
import defaults
import file_list
import display
import parse_args
import analyze

if __name__ == "__main__":
    print("Welcome to GatorGauge!")
    print("Type help to see list of commands.")
    args = parse_args.parse_args(sys.argv[1:])
    token = args.token
    while token == "":
        token = str(input("Please enter a valid token: "))
    # if there is no config.ini file, create one
    if not os.path.exists("./config.ini"):
        defaults.new_config()
        defaults.edit_config()
    defined_commands = {"help", "get", "config", "list", "analyze", "quit"}
    fSet = frozenset(defined_commands)
    specifiers = ('source', 'comments', 'commits', 'reflection')
    defined_responses = {"y", "Y", "n", "N"}
    dSet = frozenset(defined_responses)

    command = str(input('>>> '))
    args = []
    arg1 = ""
    arg2 = ""
    fileName = ""
    project = defaults.PROJECT
    keywords = str(defaults.KEYWORDS).split(',')
    out = defaults.OUT
    while command != "quit":
        args = command.rsplit()
        command = args[0]
        while args[0] not in fSet:
            print("Please enter a valid command")
            command = str(input('>>> '))
            args = command.rsplit()
            command = args[0]
            if command == "quit":
                quit()
        if len(args) == 2:
            arg1 = args[1]
        elif len(args) == 3:
            arg1 = args[1]
            arg2 = args[2]
        if command == "get":
            while project is "":
                print("You must enter a project name.")
                project = defaults.edit_config_project()
            keywords = defaults.edit_config_keywords()
            out = defaults.edit_config_directory()
            defaults.edit_config_changes()
            ask_prefix = str(
                input(
                    "Download all repositories in " +
                    project +
                    " that have " +
                    str(keywords) +
                    " in their name and place in directory '" +
                    out + "' (Y/N): "))
            while ask_prefix not in dSet:
                print("You must enter y or n.")
                ask_prefix = str(
                    input(
                        "Download all repositories in " +
                        project +
                        " that have " +
                        str(keywords) +
                        " in their name and place in directory '" +
                        out + "' (Y/N): "))
            if ask_prefix == "Y" or ask_prefix == "y":
                github_clone_all.get_repositories(
                    token, project, keywords, out)
        # allows user to edit the config file from program
        elif command == "config":
            # reset values with inputted values
            if arg1 == "edit":
                project, keywords, out = defaults.edit_config()
            elif arg1 == "reset":
                print("Config values reset")
                project = defaults.PROJECT
                keywords = str(defaults.KEYWORDS).split(',')
                out = defaults.OUT
            else:
                print("Project: " + str(project))
                print("Keywords: " + str(keywords))
                print("Out: " + str(out))
        elif command == "list":
            rep = "all"
            if arg1 is not "":
                rep = arg1
            # list of repositories or files in specified repository returned
            repo = file_list.list_files(rep, out)
            for r in repo:
                print(r)
        elif command == "analyze":
            while arg1 not in specifiers:
                print("You must enter a specifier " + str(specifiers) + ".")
                arg1 = str(input('Specifier: '))
            if arg1 == "source":
                analyze.analyze_source()
            elif arg1 == "comments":
                analyze.analyze_comments()
            elif arg1 == "commits":
                analyze.analyze_commits(out)
            elif arg1 == "reflection":
                analyze.analyze_reflection(out)
        elif command == "help":
            if arg1 == "":
                print(display.display_help())
            else:
                print(display.display_help_with_command(arg1))
        command = str(input('>>> '))
        arg1 = ""
        arg2 = ""
