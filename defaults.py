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
        config.set('Token','TOKEN',token)
    else:
        config.set('Token','TOKEN',TOKEN)
        
    ask_prefix = str(input("Would you like to edit the Project name? (Y/N): "))
    if ask_prefix is "Y" or ask_prefix is "y":
        project = ask_prefix = str(input("Enter new Project name: "))
        config.set('Project','PROJECT',project)
    else:
        config.set('Project','PROJECT',PROJECT)
        
    ask_prefix = str(input("Would you like to edit the Prefix? (Y/N): "))
    if ask_prefix is "Y" or ask_prefix is "y":
        prefix = ask_prefix = str(input("Enter new Prefix: "))
        config.set('Prefix','PREFIX',prefix)
    else:
        config.set('Prefix','PREFIX',PREFIX)
        
    ask_prefix = str(input("Would you like to edit the Out directory? (Y/N): "))
    if ask_prefix is "Y" or ask_prefix is "y":
        out = ask_prefix = str(input("Enter new Out directory: "))
        config.set('Out','OUT',out)
    else:
        config.set('Out','OUT',OUT)
 
        
    with open('./config.ini', 'w') as configFile:
        config.write(configFile)
