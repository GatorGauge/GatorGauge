"""Define strings that will be displayed by the REPL.  Used the format from Accelegator for this file"""
from colors import bold

# Help display strings
commands_list = []
commands_list.append((bold("Command"), bold("Description")))
# add help info
commands_list.append(("help", "List commands and their brief descriptions"))
commands_list.append(
    ("help <command>",
     "List verbose description of <command> and show valid arguments for <command>"))
# add get info
commands_list.append(
    ("get", "Downloads repoitories from Project with specified Prefix"))
# add config info
commands_list.append(("config", "Edit the values in the config file"))
# add list info
commands_list.append(("list", "Lists all files"))
commands_list.append(
    ("list <file>", "Lists all files with file as name or type"))
# add read info
commands_list.append(("read <file_name>",
                      "Reads the information in specified file"))
commands_list.append(("read <file_name> <location>",
                      "Reads the information in specified file in location"))
# add gensim info
commands_list.append(("gensim", "Performs NLP"))
# add quit info
commands_list.append(("quit", "Exit the program"))

# Help with command display strings
COMMANDS = ["help", "get", "config (TODO)", "list", "read", "gensim", "quit"]

# help help info
HELP_HEADER = "help\n----"
HELP_COMMAND_ONE = "help"
HELP_DESCRIPTION_ONE = "List commands and their brief descriptions"
HELP_ARGUMENTS_ONE = "None"

HELP_COMMAND_TWO = "help <command>"
HELP_DESCRIPTION_TWO = "Show verbose description of usage and show valid arguments for <command>"
HELP_ARGUMENTS_TWO = "<command>: Command to show description and valid arguments for.\nCan be any of the following:\n\t" + \
    "\n\t".join(COMMANDS)

# get help info, preparing to add other arguments
GET_HEADER = "get\n----"
GET_COMMAND_ONE = "get"
GET_DESCRIPTION_ONE = "Downloads repoitories from Project with specified Prefix to directory Out"
GET_ARGUMENTS_ONE = "None"

#TODO: add config command (edit Token, Project, Prefix, Out variables)
CONFIG_HEADER = "config\n----"
CONFIG_COMMAND = "config"
CONFIG_DESCRIPTION = "Edit the values in the config file"
CONFIG_ARGUMENTS = "None"

# list help info
LIST_HEADER = "list\n----"
LIST_COMMAND_ONE = "list"
LIST_DESCRIPTION_ONE = "List all files"
LIST_ARGUMENTS_ONE = "None"

LIST_COMMAND_TWO = "list <file>"
LIST_DESCRIPTION_TWO = "Lists all files with file as name or type"
LIST_ARGUMENTS_TWO = "<file>"

# read help info
READ_HEADER = "read\n----"
READ_COMMAND_ONE = "read <file_name>"
READ_DESCRIPTION_ONE = "Reads the information in specified file"
READ_ARGUMENTS_ONE = "<file_name>"

READ_COMMAND_TWO = "read <file_name> <location>"
READ_DESCRIPTION_TWO = "Reads the information in specified file in location"
READ_ARGUMENT_TWO = "<file_name> <location>"

# gensim help info (started, will finish with integration with repl)
GENSIM_HEADER = "gensim\n----"
GENSIM_COMMAND_ONE = "gensim"
GENSIM_DESCRIPTION_ONE = "Performs NLP"
GENSIM_ARGUMENTS_ONE = "TBD"

# quit help info
QUIT_HEADER = "quit\n----"
QUIT_COMMAND = "quit"
QUIT_DESCRIPTION = "Quits the Accelegator program"
QUIT_ARGUMENTS = "None"

COMMAND_LABEL = "Command: "
DESCRIPTION_LABEL = "Description: "
ARGUMENTS_LABEL = "Arguments: "

# Command display strings
NO_RESPONSES = "No responses to list"
