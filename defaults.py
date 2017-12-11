""" default parameters """

import configparser

CONFIG = configparser.ConfigParser()
CONFIG.read("config.ini")
PROJECT = CONFIG.get('Project', 'PROJECT')
PREFIX = CONFIG.get('Prefix', 'PREFIX')
TOKEN = CONFIG.get('Token', 'TOKEN')
OUT = CONFIG.get('Out', 'OUT')
