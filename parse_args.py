""" parse arguments inputted via command line """
import argparse


def parse_args(args):
    """ parse arguments inputted via command line """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    # specifies token for a specific repository
    parser.add_argument(
        '--token', help='GitHub API token', required=True)
    args = parser.parse_args()
    return args
