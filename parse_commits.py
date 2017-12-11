""" parse commit messages """

import pprint
from import_commits_as_string import import_commits_as_string


def number_of_commits(commit_str):
    """ return count of the number of commits """
    commit_str = import_commits_as_string("../GatorGaugeSampleRepo")
    commit_list = commit_str.split(
        "--------------------------------------------------")
    commit_count = len(commit_list)-1
    print(commit_count)
    return commit_count


def parse_commits(commit_str):
    """Breaks commit string into list"""
    commit_str = import_commits_as_string("../GatorGaugeSampleRepo")
    commit_parse_commits = commit_str.split("\n")
    commit_parse_commits[:] = [
        item for item in commit_parse_commits if item != '']
    commit_parse_commits[:] = [
        item for item in commit_parse_commits
        if item != '--------------------------------------------------']
    pprint.pprint(commit_parse_commits)
    return commit_parse_commits


def create_commit_list(commit_parse_commits, commit_count):
    """ return list of commits """
    number_commits = commit_count
    commit_commit_list = commit_parse_commits.append(number_commits)
    print(commit_commit_list)
    return commit_commit_list


create_commit_list(parse_commits("../GatorGaugeSampleRepo"), 5)
# parse_commits("../GatorGaugeSampleRepo",5)
# number_of_commits("../GatorGaugeSampleRepo")
