""" reads through and creates a list of lists from inputted file
    can be adapted to fit other group needs """
import re


def read_file(filePath):
    with open(filePath, 'r') as mark:
        # to add additional file types just use the .endswith() function to specifiy the file type
        # then add in how the file should be broken up into a list with the .split() function or
        # whatever functionality is needed
        if filePath.endswith(".md"):
            # removes newline characters and breaks up file into sentences for
            # NLP analysis
            content = mark.read()
            # removes special characters
            content = re.sub('[^a-zA-Z0-9\n\.]', ' ', content)
            content.split('. ')
    return content  # list of lists
