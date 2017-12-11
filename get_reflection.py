""" reads through and creates a list of lists from inputted file
    can be adapted to fit other group needs """

import re


def get_reflection(file_path):
    """ reads through and creates a list of lists from inputted file """
    with open(file_path, 'r') as reflection:
        # to add additional file types just use the .endswith() function to
        # specifiy the file type then add in how the file should be broken up
        # into a list with the .split() function or whatever functionality is
        # needed
        if file_path.endswith(".md"):
            # removes newline characters and breaks up file into sentences
            content = reflection.read()
            # removes special characters
            content = re.sub(r'[^a-zA-Z0-9\*\^\(\)\'\-\n\.]', ' ', content)
            content.split('. ')
    return content  # list of lists
