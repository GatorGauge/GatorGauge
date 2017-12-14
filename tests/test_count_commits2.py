import os
import sys
import count_commits.py
from dulwich.repo import Repo
from pathlib import Path

def test_path():
    """Program getting ready for testing"""
    test_path = Path("SampleRepo")
    repo_path = "SampleRepo"

    if path.is_dir():
        shutil.rmtree(path="SampleRepo", ignore_errors=Tree)

    mkdir(repo_path)
    repo = Repo.init(repo_path)
    repo = Repo(repo_path)
    repo.do_commit(b"Intial commit for sample repository")
    repo.do_commit(b"Added README.md file for lab 3")
    repo.do_commit(b"Deleted function in lab 2")
    repo.do_commit(b"Push for lab 1")
    repo.do_commit(b"Random commit XD123")

def test_commits():
    repo_commits = 5
    commits_in_repo = counted_num_commits("SampleRepo")
    assert commits_in_repo == counted_num_commits
