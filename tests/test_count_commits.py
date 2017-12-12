import os
import sys
import count_commits
from dulwich.repo import Repo
from pathlib import Path



def setup():
    """Sets up the program for testing"""
    path = Path("SampleRepo")
    repo_path = "SampleRepo"

    if path.is_dir():
            # Removes the SampleRepo if one exists
        # This is so setup() wont add double to commits to the repo
        shutil.rmtree(path="SampleRepo", ignore_errors=True)

    mkdir(repo_path)
    repo = Repo.init(repo_path)
    repo = Repo(repo_path)
    repo.do_commit(b"Initial commit")
    repo.do_commit(b"ayy lmao")
    repo.do_commit(b"added lab3")

def test_count_commits():
    expected_number_of_commits = 3
    actual_number_of_commits = count_number_of_commits("SampleRepo")
    assert actual_number_of_commits == expected_number_of_commits
