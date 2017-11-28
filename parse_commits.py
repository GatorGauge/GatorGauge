from dulwich.repo import Repo
from dulwich import porcelain
from contextlib import redirect_stdout
from io import StringIO
from import_commits_as_string import import_commits_as_string

def number_of_commits(commit_str):

	commit_list = commit_str.split("\n--------------------------------------------------")
	commit_count = len(commit_list)
	return commit_count

def parse_commits(commit_str, commit_count):

	length_of_commit_list = commit_count
	adj_commit_length = length_of_commit_list*3
	commit_commitParse = commit_string.split(":",adj_commit_length)

	return commit_commitParse

	#TODO: parse through commits for information
