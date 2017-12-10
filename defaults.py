import configparser
import os

defined_responses = {"y", "Y", "n", "N"}
fSet = frozenset(defined_responses)

config = configparser.ConfigParser(allow_no_value=True)
if os.path.exists("./config.ini"):
    config.read("config.ini")
    PROJECT = config.get('Project', 'project')
    KEYWORDS = config.get('Keywords', 'keywords')
    OUT = config.get('Out', 'out')
else:
    PROJECT = ""
    KEYWORDS = ""
    OUT = ""


def new_config():
    """Create a blank config file if one does not exist. """
    config.add_section('Project')
    config.set('Project', '; Project to pull')
    config.set('Project', 'PROJECT', "")
    config.add_section('Keywords')
    config.set(
        'Keywords',
        '; keyword list, filters down repositories exclusively')
    config.set('Keywords', 'KEYWORDS', "")
    config.add_section('Out')
    config.set('Out', '; default: repos/')
    config.set('Out', 'OUT', "repos/")

    with open('./config.ini', 'w') as config_file:
        config.write(config_file)


def edit_config_project():
    """Allow user to edit each value in the config file."""
    ask_prefix = str(
        input(
            "Current Project: '" +
            str(PROJECT) +
            "'\nWould you like to edit the Project name?\n(Y/N): "))
    while ask_prefix not in fSet:
        print("You must enter y or n.")
        ask_prefix = str(
            input(
                "Current Project: '" +
                str(PROJECT) +
                "'\nWould you like to edit the Project name?\n(Y/N): "))
    if ask_prefix is "Y" or ask_prefix is "y":
        project = ask_prefix = str(input("Enter new Project name: "))
    else:
        project = PROJECT
    return project


def edit_config_keywords():
    ask_prefix = str(
        input(
            "Current Prefix: '" +
            str(KEYWORDS) +
            "'\nWould you like to edit the Keywords?\n(Y/N): "))
    while ask_prefix not in fSet:
        print("You must enter y or n.")
        ask_prefix = str(
            input(
                "Current Prefix: '" +
                str(KEYWORDS) +
                "'\nWould you like to edit the Keywords?\n(Y/N): "))
    if ask_prefix is "Y" or ask_prefix is "y":
        keywords = ask_prefix = str(
            input("Enter new Keywords (seperated by ','): "))
    else:
        keywords = KEYWORDS
    return str(keywords).split(',')

def edit_config_directory():
    ask_prefix = str(
        input(
            "Current Out: '" +
            str(OUT) +
            "'\nWould you like to edit the Out directory?\n(Y/N): "))
    while ask_prefix not in fSet:
        print("You must enter y or n.")
        ask_prefix = str(
            input(
                "Current Out: '" +
                str(OUT) +
                "'\nWould you like to edit the Out directory?\n(Y/N): "))
    if ask_prefix is "Y" or ask_prefix is "y":
        out = ask_prefix = str(input("Enter new Out directory: "))
    else:
        out = OUT
    return out

def edit_config_changes():
    ask_prefix = str(
        input("Would you like to save these changes in config.ini?\n(Y/N): "))
    while ask_prefix not in fSet:
        print("You must enter y or n.")
        ask_prefix = str(
            input("Would you like to save these changes in config.ini?\n(Y/N): "))
    if ask_prefix is "Y" or ask_prefix is "y":
        config.set('Project', '; Project to pull')
        config.set('Project', 'PROJECT', project)
        config.set(
            'Keywords',
            '; keyword list, filters down repositories exclusively')
        config.set('Keywords', 'KEYWORDS', keywords)
        config.set('Out', '; default: repos/')
        config.set('Out', 'OUT', out)

        with open('./config.ini', 'w') as config_file:
            config.write(config_file)
