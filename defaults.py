import configparser
import os

config = configparser.ConfigParser(allow_no_value=True)
if os.path.exists("./config.ini"):
    config.read("config.ini")
    TOKEN = config.get('Token', 'token')
    PROJECT = config.get('Project', 'project')
    KEYWORDS = config.get('Keywords', 'keywords')
    OUT = config.get('Out', 'out')

# creates a blank config file if one does not exist
def newConfig():
    config.add_section('Token')
    config.set('Token', '; Github access token KEEP SECRET!!!!')
    config.set('Token', 'TOKEN', "")
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

    with open('./config.ini', 'w') as configFile:
            config.write(configFile)

# allows user to edit each value in the config file    
def editConfig():
    ask_prefix = str(
        input(
            "Current Token: '" +
            str(TOKEN) +
            "'\nWould you like to edit the Token?\n(Y/N): "))
    if ask_prefix is "Y" or ask_prefix is "y":
        token = ask_prefix = str(input("Enter new Token: "))
    else:
        token = TOKEN

    ask_prefix = str(
        input(
            "Current Project: '" +
            str(PROJECT) +
            "'\nWould you like to edit the Project name?\n(Y/N): "))
    if ask_prefix is "Y" or ask_prefix is "y":
        project = ask_prefix = str(input("Enter new Project name: "))
    else:
        project = PROJECT

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

    ask_prefix = str(
        input(
            "Current Out: '" +
            str(OUT) +
            "'\nWould you like to edit the Out directory?\n(Y/N): "))
    if ask_prefix is "Y" or ask_prefix is "y":
        out = ask_prefix = str(input("Enter new Out directory: "))
    else:
        out = OUT
    
    ask_prefix = str(
        input("Would you like to save these changes in config.ini?\n(Y/N): "))

    if ask_prefix is "Y" or ask_prefix is "y":
        config.set('Token', '; Github access token KEEP SECRET!!!!')
        config.set('Token', 'TOKEN', token)
        config.set('Project', '; Project to pull')
        config.set('Project', 'PROJECT', project)
        config.set(
            'Keywords',
            '; keyword list, filters down repositories exclusively')
        config.set('Keywords', 'KEYWORDS', keywords)
        config.set('Out', '; default: repos/')
        config.set('Out', 'OUT', out)

        with open('./config.ini', 'w') as configFile:
            config.write(configFile)
    return token, project, str(keywords).split(','), out
