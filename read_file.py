""" reads through and creates a list of lists from inputted file """
import re

def read_file(File):
    content = list()
    with open(File,'r') as mark:
        if File.endswith(".md") or File.endswith(".txt"):
            lines = mark.read().replace("\n"," ").split('. ') # removes newline characters and breaks up file into sentences
        elif File.endswith(".java"):
            lines = mark.read().split('\n')
        else:
            lines = mark.read().split('\n')
    for line in lines:
        # if File.endswith('README.md'): # formats README.md output, uncomment if needed
            # line = re.sub(r'(?s)(#)(.*?)(  )', '', line).strip() # annoying line, removes section headers from README.md files 
        nextLine = list()                                     # (unnecessary but leaving in just in case)
        if not line == '':
            nextLine.append(line)
            content.append(nextLine)
    return content # list of lists
