""" reads through and creates a list of lists from inputted file
    can be adapted to fit other group needs """
import re


def get_reflection(filePath):
    with open(filePath, 'r') as reflection:
        # to add additional file types just use the .endswith() function to specifiy the file type
        # then add in how the file should be broken up into a list with the .split() function or
        # whatever functionality is needed
        if filePath.endswith(".md"):
            # removes newline characters and breaks up file into sentences for
            # NLP analysis
            content = reflection.read()
            # removes special characters
            content = re.sub('[^a-zA-Z0-9\*\^\(\)\'\-\n\.]', ' ', content)
            content.split('. ')
    return content  # list
