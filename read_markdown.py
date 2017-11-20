""" reads through and creates a list of lists for markdown files """
import re

def read_markdown(File):
    content = list()
    with open(File,'r') as mark:
        lines = mark.read().replace("\n"," ").replace("-","").split('. ') # removes
    for line in lines:
        line = re.sub(r'(?s)(#)(.*?)(  )', '', line).strip() # annoying line, removes section headers
        nextLine = list()
        if not line == '':
            nextLine.append(line)
            content.append(nextLine)
    return content
