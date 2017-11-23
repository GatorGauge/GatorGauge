import defaults

def repl():

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
            if ask_prefix is "Y" or "y":
                prefix = str(input("Enter the prefix for the repo: "))
            elif ask_prefix is "N" or "n":
                prefix = defaults.PREFIX
            ask_out = str(input("Would you like to specify the destiantion? (Y/N): "))
            while ask_out not in rSet:
                ask_out = str(input("Please enter Y or N: "))
            if ask_out is "Y" or "y":
                ask_out = str(input("Enter the destination: "))
            elif ask_out is "N" or "n":
                out = default.OUT
            return project, prefix, token, out
        elif command == "help":
            print("help")
        command = str(input('>>> '))
        while command not in fSet:
            print("Please enter a valid command")
            command = str(input('>>> '))
