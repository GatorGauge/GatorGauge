from dulwich.repo import Repo
from dulwich import porcelain
from contextlib import redirect_stdout
from io import StringIO

def import_commits_as_string(file_path):


	#Constants
	NEW_OUTSTREAM = StringIO()
	
	commit_str = ""

	#Opens repo at this file
	path = file_path

	#sets repo to open from file_path
	repo = Repo(file_path)

	#porcelain handles the reading of the file at file_path
	print("Reading commit for: " + file_path)

	#Porcelain automatically writes to the terminal, to override this we must redirect the stdout with our new outstream saved in NEW_OUTSTREAM.  This allows us to save the log as a string so we can manipulate it.
	
	with redirect_stdout(NEW_OUTSTREAM):
		porcelain.log(repo)
	
	commit_str = f.getvalue()
	
	return commit_str

def generate_list_of_commits(str_of_commits):
	

	

def print_commit(commit, decode, outstream=sys.stdout):
	"""Write a human-readable commit log entry.
    :param commit: A `Commit` object
    :param outstream: A stream file to write to
    """
    outstream.write("-" * 50 + "\n")
    outstream.write("commit: " + commit.id.decode('ascii') + "\n")
    if len(commit.parents) > 1:
        outstream.write(
            "merge: " +
            "...".join([c.decode('ascii') for c in commit.parents[1:]]) + "\n")
    outstream.write("Author: " + decode(commit.author) + "\n")
    if commit.author != commit.committer:
        outstream.write("Committer: " + decode(commit.committer) + "\n")

    time_tuple = time.gmtime(commit.author_time + commit.author_timezone)
    time_str = time.strftime("%a %b %d %Y %H:%M:%S", time_tuple)
    timezone_str = format_timezone(commit.author_timezone).decode('ascii')
    outstream.write("Date:   " + time_str + " " + timezone_str + "\n")
    outstream.write("\n")
    outstream.write(decode(commit.message) + "\n")
outstream.write("\n")

	

