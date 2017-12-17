"""Parse commit messages."""
import os

from contextlib import redirect_stdout
from io import StringIO
from dulwich.repo import Repo
from dulwich import porcelain


def get_commits_for_all_repos(out):
    """Get commits as strings for all repos."""
    names_of_repos = next(os.walk("./" + str(out)))[1]
    commits = []

    for repo in names_of_repos:
        with porcelain.open_repo_closing("./" + str(out) + "/" + str(repo)) as repo:
            walker = repo.get_walker(reverse=True)
        for entry in walker:
            item = str(entry.commit.message.decode())
            item = item.replace("\n", "")
            commits.append(item)

    return commits


def get_list_of_each_commit(list_of_commit_strings):
    """Split each string in list on each commit and append to list of each commit."""
    list_of_each_commit = []
    for commit_string in list_of_commit_strings:
        commits = commit_string.split("\n")
        commits[:] = [
            item for item in commits if item != '']
        commits[:] = [
            item for item in commits
            if item != '--------------------------------------------------']
        for commit in commits:
            list_of_each_commit.append(commit)

    return list_of_each_commit


def get_list_of_commits(out):
    """Return list of commits for all repos."""
    return get_list_of_each_commit(get_commits_for_all_repos(out))
