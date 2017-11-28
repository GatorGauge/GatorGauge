from dulwich.repo import Repo
from dulwich import porcelain
from contextlib import redirect_stdout
from io import StringIO
from import_commits_as_string import import_commits_as_string
import pprint

def number_of_commits(commit_str):

	commit_str = import_commits_as_string("../GatorGaugeSampleRepo")
	commit_list = commit_str.split("--------------------------------------------------")
	commit_count = len(commit_list)-1
	print(commit_count)
	return commit_count

def parse_commits(commit_str):
	"""Breaks commit string into list"""
	commit_str = import_commits_as_string("../GatorGaugeSampleRepo")
	commit_parseCommits = commit_str.split("\n")
	commit_parseCommits[:] = [item for item in commit_parseCommits if item != '']
	commit_parseCommits[:] = [item for item in commit_parseCommits if item != '--------------------------------------------------']
	pprint.pprint(commit_parseCommits)

	return commit_parseCommits

def create_commitList(commit_parseCommits, commit_count):
	number_of_commits = commit_count
	commit_commitList = commit_parseCommits.append(number_of_commits)
	print(commit_commitList)

	return commit_commitList

create_commitList(parse_commits("../GatorGaugeSampleRepo"),5)
#parse_commits("../GatorGaugeSampleRepo",5)
#number_of_commits("../GatorGaugeSampleRepo")
