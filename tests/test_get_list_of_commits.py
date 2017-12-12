from analyze_commits import get_list_of_commits
from dulwich.repo import Repo
from pathlib import Path
from os import mkdir
import shutil


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


def test_get_list_of_commits():
    """Test the functionality of getting_list_of_commits"""
    list = []
    list = (get_list_of_commits("./SampleRepo"))
    assert len(list) == 3
    assert "Initial commit" in list
    assert "added lab3" in list
