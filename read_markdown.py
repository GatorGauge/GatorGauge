""" reads through and creates a list of lists for markdown files """
import re

def read_markdown(File):
    content = list()
    with open(File,'r') as mark:
        lines = mark.read().replace("\n"," ").replace("-","").split('. ')
    for line in lines:
        re.sub(r' #.*?  ', '', line)
        nextLine = list()
        if not line == '':
            nextLine.append(line)
            content.append(nextLine)
    return content
