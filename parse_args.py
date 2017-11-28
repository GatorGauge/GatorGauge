""" parse arguments inputted via command line """
import argparse

import defaults #get defaults form defaults.py

def parse_args(args): #creates command line arguments for easier access to repositories
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--get', #downloads repositories: defaults are used if no prefix or project is specified
                            default=False,
                            help="Download the repositories.\nIf not default project or prefix, must use '--project' or '--prefix'",
                            action="store_true")

    parser.add_argument('--list', #lists files
                            default=".",
                            const="all",
                            nargs='?',
                            help="List the files with the given extension")

    parser.add_argument('--read', #reads information from a file
                            default="",
                            help="Read the information in a given file")

    parser.add_argument('--project', #specifies a specific project within the repositories
                            default=defaults.PROJECT,
                            help='GitHub project to scan, default: ' + defaults.PROJECT)

    parser.add_argument('--prefix', #finds projects with the same prefix for analysis
                            default=defaults.PREFIX,
                            help='Prefix on projects to match (default: match all projects)')

    parser.add_argument('--token', #specifies token for a specific repository
                            default=defaults.TOKEN,
                            help='GitHub API token')

    parser.add_argument('--out', #directory for which the repositories will be placed
                            default=defaults.OUT,
                            help='Destination directory for GitHub clones (default: current directory)')

    args = parser.parse_args()

    return args
