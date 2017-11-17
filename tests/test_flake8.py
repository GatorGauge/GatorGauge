import glob
import os
from flake8.api import legacy as flake8


# Testing the python file for flake8 standards
def test_flake8():

    # list of all file names to be checked for PEP8
    name_of_files = []

    # fill list with all python files found in all subdirectories
    for root, dirs, files in os.walk("accelegator", topdown=False):
        files = glob.glob(root + "/*.py")
        name_of_files.extend(files)

    style_guide = flake8.get_style_guide(ignore=["E265", "E501"])
    report = style_guide.check_files(name_of_files)
    assert report.get_statistics('E') == [], 'Flake8 found violations'
