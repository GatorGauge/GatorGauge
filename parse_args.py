""" parse arguments inputted via command line """
import argparse

import defaults  # get defaults form defaults.py

# creates command line arguments for easier access to repositories



def parse_args(args):
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # downloads repositories: defaults are used if no prefix or project is
    # specified
    parser.add_argument(
        '--get',
        default=False,
        help="Download the repositories.\nIf not default project or prefix, must use '--project' or '--prefix'",
        action="store_true")

    # lists files
    parser.add_argument('--list',
                        default=".",
                        const="all",
                        nargs='?',
                        help="List the files with the given extension")

    # reads information from a file
    parser.add_argument('--read',
                        default="",
                        help="Read the information in a given file")

    # specifies a specific project within the repositories
    parser.add_argument(
        '--project',
        default=defaults.PROJECT,
        help='GitHub project to scan, default: ' +
        defaults.PROJECT)

    # finds projects with the same prefix for analysis
    parser.add_argument(
        '--prefix',
        default=defaults.PREFIX,
        help='Prefix on projects to match (default: match all projects)')

    # specifies token for a specific repository
    parser.add_argument('--token',
                        default=defaults.TOKEN,
                        help='GitHub API token')

    # directory for which the repositories will be placed
    parser.add_argument(
        '--out',
        default=defaults.OUT,
        help='Destination directory for GitHub clones (default: current directory)')

    args = parser.parse_args()

    return args
