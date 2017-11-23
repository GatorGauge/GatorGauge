import sys

import github_clone_all
import parse_args
import defaults
if __name__ == "__main__":

#    args = parse_args.parse_args(sys.argv[1:])

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
            token = str(input("Enter the token for the repo: "))
            project = str(input("Enter the name of the project: "))
            ask_prefix = str(input("Would you like to specify a prefix? (Y/N): "))
            while ask_prefix not in rSet:
                ask_prefix = str(input("Please enter Y or N: "))
            if ask_prefix == "Y" or ask_prefix == "y":
                prefix = str(input("Enter the prefix for the repo: "))
            elif ask_prefix == "N" or ask_prefix == "n":
                prefix = defaults.PREFIX
            ask_out = str(input("Would you like to specify the destiantion? (Y/N): "))
            while ask_out not in rSet:
                ask_out = str(input("Please enter Y or N: "))
            if ask_out == "Y" or ask_out == "y":
                ask_out = str(input("Enter the destination: "))
            elif ask_out == "N" or ask_out == "n":
                out = default.OUT
            github_clone_all.get_repositories(project, prefix, token, out)
        elif command == "help":
            print("help")
        command = str(input('>>> '))
        while command not in fSet:
            print("Please enter a valid command")
            command = str(input('>>> '))

#    print(args)
#    if args.get is True and defaults.PROJECT == "" and args.project == "":
#        print("\tERROR: '--get' requires either a default project name or a supplied '--project' flag")
#        quit()
#    if args.get is True:
#        github_clone_all.get_repositories(args.project, args.prefix, args.token, args.out)
