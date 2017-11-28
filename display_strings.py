"""Define strings that will be displayed by the REPL."""
"""Used the format from Accelegator for this file"""
from colors import bold

# Help display strings
commands_list = []

commands_list.append((bold("Command"), bold("Description")))
commands_list.append(("help", "List commands and their brief descriptions"))
commands_list.append(("help <command>", "List verbose description of <command> and show valid arguments for <command>"))
commands_list.append(("get", "Downloads repoitories from Project with specified Prefix"))
commands_list.append(("list", "Lists all files"))
commands_list.append(("list <file>", "Lists all files with file as name or type"))
commands_list.append(("read <file_name>", "Reads the information in specified file"))
commands_list.append(("read <file_name> <location>", "Reads the information in specified file in location"))
commands_list.append(("quit", "Exit the program"))

# Help with command display strings
COMMANDS = ["help", "get", "list", "read", "quit"]
HELP_HEADER = "help\n----"
HELP_COMMAND_ONE = "help"
HELP_DESCRIPTION_ONE = "List commands and their brief descriptions"
HELP_ARGUMENTS_ONE = "None"

HELP_COMMAND_TWO = "help <command>"
HELP_DESCRIPTION_TWO = "Show verbose description of usage and show valid arguments for <command>"
HELP_ARGUMENTS_TWO = "<command>: Command to show description and valid arguments for.\nCan be any of the following\n\t" + "\n\t".join(COMMANDS)

GET_HEADER = "get\n----"
GET_COMMAND = "get"
GET_DESCRIPTION = "Downloads repoitories from Project with specified Prefix"
GET_ARGUMENTS = "None"

LIST_HEADER = "list\n----"
LIST_COMMAND_ONE = "list"
LIST_DESCRIPTION_ONE = "List all files"
LIST_ARGUMENTS_ONE = "None"

LIST_COMMAND_TWO = "list <file>"
LIST_DESCRIPTION_TWO = "Lists all files with file as name or type"
LIST_ARGUMENTS_TWO = "<file>"

READ_HEADER = "read\n----"
READ_COMMAND_ONE = "read <file_name>"
READ_DESCRIPTION_ONE = "Reads the information in specified file"
READ_ARGUMENTS_ONE = "<file_name>"

READ_COMMAND_TWO = "read <file_name> <location>"
READ_DESCRIPTION_TWO = "Reads the information in specified file in location"
READ_ARGUMENT_TWO = "<file_name> <location>"

QUIT_HEADER = "quit\n----"
QUIT_COMMAND = "quit"
QUIT_DESCRIPTION = "Quits the Accelegator program"
QUIT_ARGUMENTS = "None"

COMMAND_LABEL = "Command: "
DESCRIPTION_LABEL = "Description: "
ARGUMENTS_LABEL = "Arguments: "

# Command display strings
NO_RESPONSES = "No responses to list"
