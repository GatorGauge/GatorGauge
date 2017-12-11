""" imports commits as string """

from contextlib import redirect_stdout
from io import StringIO
from dulwich.repo import Repo
from dulwich import porcelain


def import_commits_as_string(file_path):
    """ function takes in a file_path, points to a given repo """

    # Constants
    new_outstream = StringIO()

    # Future string of commits
    commit_str = ""

    # sets repo to open from file_path
    repo = Repo(file_path)

    # Porcelain automatically writes to the terminal, to override this we must
    # redirect the stdout with our new outstream saved in NEW_OUTSTREAM.  This
    # allows us to save the log as a string so we can manipulate it.

    with redirect_stdout(new_outstream):
        porcelain.log(repo, outstream=new_outstream)

    commit_str = new_outstream.getvalue()

    return commit_str
