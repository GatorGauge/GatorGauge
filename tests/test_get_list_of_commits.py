from get_list_of_commits import get_list_of_commits
from dulwich.repo import Repo
from pathlib import Path
from os import mkdir
import shutil

"""Removes the SampleRepo if one exists"""
"""This is so setup() wont add double to commits to the repo"""
shutil.rmtree("SampleRepo")

def setup():
    file_path = Path("SampleRepo")

    if not (file_path.is_dir()):
        mkdir("SampleRepo")
        repo = Repo.init("SampleRepo")

    repo = Repo("SampleRepo")
    repo.do_commit(b"Initial commit")
    repo.do_commit(b"ayy lmao")
    repo.do_commit(b"added lab3")

def test_get_list_of_commits():
    """Test the functionality of getting_list_of_commits"""
    list = []
    list = (get_list_of_commits("SampleRepo"))
    assert len(list) == 3
    assert "Initial commit" in list
    assert "added lab3" in list
