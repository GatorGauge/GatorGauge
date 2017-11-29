import configparser

config = configparser.ConfigParser()
config.read("config.ini")
PROJECT = config.get('Project', 'PROJECT')
PREFIX = config.get('Prefix', 'PREFIX')
TOKEN = config.get('Token', 'TOKEN')
OUT = config.get('Out', 'OUT')
