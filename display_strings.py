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
    ("get", "Downloads repositories from Project with specified Prefix to directory Out"))
# add config info
commands_list.append(("config", "Edit the values in the config file"))
# add list info
commands_list.append(("list", "Lists all files"))
commands_list.append(
    ("list <repo name>", "Lists all files in the inputted repository"))
# add analyze info
commands_list.append(
    ("analyze <target>", "Performs analysis for specified target ('source','comments','commits','reflection')"))
# add quit info
commands_list.append(("quit", "Exit the program"))

# Help with command display strings
COMMANDS = ["help", "get", "config", "list", "analyze", "quit"]

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
GET_DESCRIPTION_ONE = "Downloads repositories from Project with specified Prefix to directory Out"
GET_ARGUMENTS_ONE = "None"

# config help info
CONFIG_HEADER = "config\n----"
CONFIG_COMMAND = "config"
CONFIG_DESCRIPTION = "Edit the values in the config file"
CONFIG_ARGUMENTS = "None"

# list help info
LIST_HEADER = "list\n----"
LIST_COMMAND_ONE = "list"
LIST_DESCRIPTION_ONE = "List all repositories"
LIST_ARGUMENTS_ONE = "None"

LIST_COMMAND_TWO = "list <repo name>"
LIST_DESCRIPTION_TWO = "Lists all files in the given repository"
LIST_ARGUMENTS_TWO = "<repo name>"

# gensim help info (started, will finish with integration with repl)
ANALYZE_HEADER = "analyze\n----"
ANALYZE_COMMAND_ONE = "analyze <target>"
ANALYZE_DESCRIPTION_ONE = "Performs analysis for specified target ('source','comments','commits','reflection')"
ANALYZE_ARGUMENTS_ONE = "<target>"

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
