import configparser

config = configparser.ConfigParser()
config.read("config.ini")
PROJECT = config.get('Project', 'PROJECT')
PREFIX = config.get('Prefix', 'PREFIX')
TOKEN = config.get('Token', 'TOKEN')
OUT = config.get('Out', 'OUT')


def editConfig():
    ask_prefix = str(input("Would you like to edit the Token? (Y/N): "))
    if ask_prefix is "Y" or ask_prefix is "y":
        token = ask_prefix = str(input("Enter new Token: "))
    else:
        token = TOKEN

    ask_prefix = str(input("Would you like to edit the Project name? (Y/N): "))
    if ask_prefix is "Y" or ask_prefix is "y":
        project = ask_prefix = str(input("Enter new Project name: "))
    else:
        project = PROJECT

    ask_prefix = str(input("Would you like to edit the Prefix? (Y/N): "))
    if ask_prefix is "Y" or ask_prefix is "y":
        prefix = ask_prefix = str(input("Enter new Prefix: "))
    else:
        prefix = PREFIX

    ask_prefix = str(input("Would you like to edit the Out directory? (Y/N): "))
    if ask_prefix is "Y" or ask_prefix is "y":
        out = ask_prefix = str(input("Enter new Out directory: "))
    else:
        out = OUT

    ask_prefix = str(input("Would you like to save these changes in config.ini? (Y/N): "))
    if ask_prefix is "Y" or ask_prefix is "y":
        config.set('Token', 'TOKEN', token)
        config.set('Project', 'PROJECT', project)
        config.set('Prefix', 'PREFIX', prefix)
        config.set('Out', 'OUT', out)
        with open('./config.ini', 'w') as configFile:
            config.write(configFile)
    return token, project, prefix, out
