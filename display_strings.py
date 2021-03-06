"""Define strings that will be displayed by the REPL.  Used the format from
Accelegator for this file"""

from colors import bold

# Help display strings
COMMANDS_LIST = []
COMMANDS_LIST.append((bold("Command"), bold("Description")))
# add help info
COMMANDS_LIST.append(("help", "List commands and their brief descriptions"))
COMMANDS_LIST.append(
    ("help <command>", "List verbose description of <command> " +
     "and show valid arguments for <command>"))
# add get info
COMMANDS_LIST.append(
    ("get", "Downloads repositories from Project " +
     "with specified Prefix to directory Out"))
# add config info
COMMANDS_LIST.append(("config", "Print the values in the config file"))
COMMANDS_LIST.append(
    ("config <option>",
     "Edit or refresh the values in the config file, type 'help config' for more details"))
# add list info
COMMANDS_LIST.append(("list", "Lists all files"))
COMMANDS_LIST.append(
    ("list <repo name>", "Lists all files in the inputted repository"))
# add analyze info
COMMANDS_LIST.append(
    ("analyze <target>", "Performs analysis for specified target " +
     "('source','comments','commits','reflection')"))
# add quit info
COMMANDS_LIST.append(("quit", "Exit the program"))

# Help with command display strings
COMMANDS = ["help", "get", "config", "list", "analyze", "quit"]

# help help info
HELP_HEADER = "help\n----"
HELP_COMMAND_ONE = "help"
HELP_DESCRIPTION_ONE = "List commands and their brief descriptions"
HELP_ARGUMENTS_ONE = "None"

HELP_COMMAND_TWO = "help <command>"
HELP_DESCRIPTION_TWO = \
    "Show verbose description of usage " + \
    "and show valid arguments for <command>"
HELP_ARGUMENTS_TWO = \
    "<command>: Command to show description " + \
    "and valid arguments for.\nCan be any of the following:\n\t" + \
    "\n\t".join(COMMANDS)

# get help info, preparing to add other arguments
GET_HEADER = "get\n----"
GET_COMMAND_ONE = "get"
GET_DESCRIPTION_ONE = \
    "Downloads repositories from Project " + \
    "with specified Prefix to directory Out"
GET_ARGUMENTS_ONE = "None"

# config help info
CONFIG_HEADER = "config\n----"
CONFIG_COMMAND_ONE = "config"
CONFIG_DESCRIPTION_ONE = "show the values in the config file"
CONFIG_ARGUMENTS_ONE = "None"

CONFIG_COMMAND_TWO = "config <option>"
CONFIG_DESCRIPTION_TWO = "Edit or refresh the values in the config file"
CONFIG_ARGUMENTS_TWO = "<option>: 'edit'- modify the values in the config or 'refresh'- reset the values (used if the values are not saved into the config or the config is manually updated)"

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
ANALYZE_DESCRIPTION_ONE = "Performs analysis for specified target "
ANALYZE_ARGUMENTS_ONE = "<target>: 'source', 'comments', 'commits', or 'reflection'"

# quit help info
QUIT_HEADER = "quit\n----"
QUIT_COMMAND = "quit"
QUIT_DESCRIPTION = "Quits GatorGauge"
QUIT_ARGUMENTS = "None"

COMMAND_LABEL = "Command: "
DESCRIPTION_LABEL = "Description: "
ARGUMENTS_LABEL = "Arguments: "

# Command display strings
NO_RESPONSES = "No responses to list"
