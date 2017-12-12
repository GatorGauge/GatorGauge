""" configuration defaults and modifications """

import configparser

GENSIM_OUTPUT_FILENAME = "vis.html"

defined_responses = {"y", "Y", "n", "N"}
fSet = frozenset(defined_responses)

config = configparser.ConfigParser(allow_no_value=True)
config.read("config.ini")
#PROJECT = ""
#KEYWORDS = ""
#OUT = "repos/"

GENSIM_HTML_OUT = "vis.html"


def get_project():
    PROJECT = config.get('Project', 'project')
    return PROJECT


def get_keywords():
    KEYWORDS = config.get('Keywords', 'keywords')
    return KEYWORDS


def get_out():
    OUT = config.get('Out', 'out')
    return OUT


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
    config.add_section('Setup')

    with open('./config.ini', 'w') as config_file:
        config.write(config_file)
    project = edit_config_project()
    keywords = edit_config_keywords()
    out = edit_config_directory()
    save_config_changes(project, keywords, out)


def edit_config():
    """Allow user to edit each value in the config file."""
    ask_prefix = str(
        input(
            "Current Project: '" +
            str(get_project()) +
            "'\nWould you like to edit the Project name?\n(Y/N): "))
    while ask_prefix not in fSet:
        print("You must enter y or n.")
        ask_prefix = str(
            input(
                "Current Project: '" +
                str(get_project()) +
                "'\nWould you like to edit the Project name?\n(Y/N): "))
    if ask_prefix is "Y" or ask_prefix is "y":
        project = ask_prefix = str(input("Enter new Project name: "))
    else:
        project = config.get('Project', 'project')
    return project


def edit_config_keywords():
    ask_prefix = str(
        input(
            "Current keywords: '" +
            str(get_keywords()) +
            "'\nWould you like to edit the Keywords?\n(Y/N): "))
    while ask_prefix not in fSet:
        print("You must enter y or n.")
        ask_prefix = str(
            input(
                "Current Prefix: '" +
                str(get_keywords()) +
                "'\nWould you like to edit the Keywords?\n(Y/N): "))
    if ask_prefix is "Y" or ask_prefix is "y":
        keywords = ask_prefix = str(
            input("Enter new Keywords (seperated by ','): "))
    else:
        keywords = config.get('Keywords', 'keywords')
    return keywords


def edit_config_directory():
    ask_prefix = str(
        input(
            "Current Out: '" +
            str(get_out()) +
            "'\nWould you like to edit the Out directory?\n(Y/N): "))
    while ask_prefix not in fSet:
        print("You must enter y or n.")
        ask_prefix = str(
            input(
                "Current Out: '" +
                str(get_out()) +
                "'\nWould you like to edit the Out directory?\n(Y/N): "))
    if ask_prefix is "Y" or ask_prefix is "y":
        out = ask_prefix = str(input("Enter new Out directory: "))
    else:
        out = config.get('Out', 'out')
    return out


def save_config_changes(project, keywords, out):
    if config.has_section('Setup'):
        config.remove_section('Setup')
        ask_prefix = "Y"
    else:
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
        config.read("config.ini")
        #PROJECT = config.get('Project', 'project')
        #KEYWORDS = config.get('Keywords', 'keywords')
        #OUT = config.get('Out', 'out')
