from dulwich.repo import Repo
from dulwich import porcelain
from contextlib import redirect_stdout
from io import StringIO

#function takes in a file_path, points to a given repo
def get_list_of_commits(file_path):

    # Constants
    NEW_OUTSTREAM = StringIO()

    # Future string of commits
    commit_str = ""
    new_str_list = list()
	
    # Opens repo at this file
    path = file_path

    # sets repo to open from file_path
    repo = Repo(file_path)

    # Porcelain automatically writes to the terminal, to override this we must
    # redirect the stdout with our new outstream saved in NEW_OUTSTREAM.  
    # This allows us to save the log as a string so we can manipulate it.

    with redirect_stdout(NEW_OUTSTREAM):
        porcelain.log(repo, outstream = NEW_OUTSTREAM, reverse = True)
		
    commit_str = NEW_OUTSTREAM.getvalue()
	
	
    for line in commit_str.splitlines():
        if 'commit: ' not in line and 'Author: ' not in line and 'Date' not in line and '----------' not in line and 'Committer: ' not in line:
            new_str_list.append(line)
	
    while '' in new_str_list:
        new_str_list.remove('')
	
    return new_str_list