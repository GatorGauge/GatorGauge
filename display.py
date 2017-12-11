"""Format and return strings to display.  Used the format from Accelegator for this file"""
from colors import bold
import logging
import textwrap
# local import
import display_strings


def display_help_with_command(command):
    """Return a string with verbose description and valid arguments for a command."""
    command_functions = {
        "help": display_help_help,
        "get": display_get_help,
        "config": display_config_help,
        "list": display_list_help,
        "analyze": display_analyze_help,
        "quit": display_quit_help
    }

    return command_functions[command]()


def display_help_help():
    command_one_tuple = (display_strings.HELP_HEADER,
                         display_strings.HELP_COMMAND_ONE,
                         display_strings.HELP_DESCRIPTION_ONE,
                         display_strings.HELP_ARGUMENTS_ONE)
    logging.debug("Command one details: " + str(command_one_tuple))

    command_two_tuple = (display_strings.HELP_COMMAND_TWO,
                         display_strings.HELP_DESCRIPTION_TWO,
                         display_strings.HELP_ARGUMENTS_TWO)
    logging.debug("Command two details: " + str(command_two_tuple))

    return format_command_description(command_one_tuple, command_two_tuple)


def display_get_help():
    command_tuple = (display_strings.GET_HEADER,
                     display_strings.GET_COMMAND_ONE,
                     display_strings.GET_DESCRIPTION_ONE,
                     display_strings.GET_ARGUMENTS_ONE)

    logging.debug("Command one details: " + str(command_tuple))

    return format_command_description(command_tuple)


def display_config_help():
    command_one_tuple = (display_strings.CONFIG_HEADER,
                         display_strings.CONFIG_COMMAND_ONE,
                         display_strings.CONFIG_DESCRIPTION_ONE,
                         display_strings.CONFIG_ARGUMENTS_ONE)

    logging.debug("Command one details: " + str(command_one_tuple))

    command_two_tuple = (display_strings.CONFIG_COMMAND_TWO,
                         display_strings.CONFIG_DESCRIPTION_TWO,
                         display_strings.CONFIG_ARGUMENTS_TWO)

    logging.debug("Command one details: " + str(command_two_tuple))

    return format_command_description(command_one_tuple, command_two_tuple)


def display_list_help():
    command_one_tuple = (display_strings.LIST_HEADER,
                         display_strings.LIST_COMMAND_ONE,
                         display_strings.LIST_DESCRIPTION_ONE,
                         display_strings.LIST_ARGUMENTS_ONE)
    logging.debug("Command details: " + str(command_one_tuple))

    command_two_tuple = (display_strings.LIST_COMMAND_TWO,
                         display_strings.LIST_DESCRIPTION_TWO,
                         display_strings.LIST_ARGUMENTS_TWO)
    logging.debug("Command two details: " + str(command_two_tuple))

    return format_command_description(
        command_one_tuple, command_two_tuple)


def display_analyze_help():
    command_one_tuple = (display_strings.ANALYZE_HEADER,
                         display_strings.ANALYZE_COMMAND_ONE,
                         display_strings.ANALYZE_DESCRIPTION_ONE,
                         display_strings.ANALYZE_ARGUMENTS_ONE)
    logging.debug("Command one details: " + str(command_one_tuple))

    return format_command_description(command_one_tuple)


def display_quit_help():
    command_tuple = (display_strings.QUIT_HEADER,
                     display_strings.QUIT_COMMAND,
                     display_strings.QUIT_DESCRIPTION,
                     display_strings.QUIT_ARGUMENTS)

    return format_command_description(command_tuple)


def format_command_description(
        command_one_tuple,
        command_two_tuple=None,
        command_three_tuple=None,
        command_four_tuple=None):
    logging.info("Formatting first command")
    header = bold(command_one_tuple[0])
    command_one = command_one_tuple[1]
    description_one = command_one_tuple[2]
    arguments_one = command_one_tuple[3]
    command_one_string = header + "\n" + display_strings.COMMAND_LABEL + command_one + "\n" + \
        display_strings.DESCRIPTION_LABEL + description_one + "\n" + \
        display_strings.ARGUMENTS_LABEL + arguments_one + "\n"

    if command_two_tuple is not None:
        logging.info("Formatting second command")
        command_two = command_two_tuple[0]
        description_two = command_two_tuple[1]
        arguments_two = command_two_tuple[2]
        command_two_string = display_strings.COMMAND_LABEL + command_two + "\n" + display_strings.DESCRIPTION_LABEL + \
            description_two + "\n" + display_strings.ARGUMENTS_LABEL + arguments_two + "\n"
        return command_one_string + "\n" + command_two_string
    else:
        return command_one_string


def display_help():
    """Return a string with a list of commands and their brief descriptions."""
    logging.info("Creating help string")

    help_string = ""

    for current_index, command_tuple in enumerate(
            display_strings.commands_list):
        left = command_tuple[0]
        right = command_tuple[1]
        if current_index is 0:
            # accounts for ansi sequence for bolded text in header
            help_string += "{:<38s}{:<40s}".format(left, right) + "\n"
        else:
            right_list = (textwrap.wrap(right, width=40))
            for current_line, description_line in enumerate(right_list):
                if current_line is 0:
                    help_string += "{:<30s}{:<40s}".format(
                        left, description_line) + "\n"
                else:
                    empty_space = ""
                    description_line = "\t" + description_line
                    help_string += "{:<30s}{:<40s}".format(
                        empty_space, description_line) + "\n"

    return help_string


def align(left, right, is_negative_timestamp=False):
    """Return string with "left" aligned to the left and "right" aligned to the right."""
    if is_negative_timestamp:
        logging.debug(
            "Moving right over 8 characters to account for ansi sequence")
        # adjust right alignment of inverted timestamp to account for ansi
        # sequence
        return "{:<40s}{:>48s}".format(left, right)
    else:
        return "{:<40s}{:>40s}".format(left, right)
