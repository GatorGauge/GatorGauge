from dulwich.repo import Repo
from dulwich import porcelain
from contextlib import redirect_stdout
from io import StringIO
from import_commits_as_string import import_commits_as_string

def number_of_commits(commit_str):

	commit_list = commit_str.split("\n--------------------------------------------------")
	commit_count = len(commit_list)
	return commit_count

def parse_commits(commit_str):

	#TODO: parse through commits for information