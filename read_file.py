""" reads through and creates a list of lists from inputted file """
""" can be adapted to fit other group needs """

def read_file(filePath):
    content = list()
    with open(filePath, 'r') as mark:
        # to add additional file types just use the .endswith() function to specifiy the file type
        # then add in how the file should be broken up into a list with the .split() function or
        # whatever functionality is needed
        if filePath.endswith(".md"):
            # removes newline characters and breaks up file into sentences for
            # NLP analysis
            lines = mark.read().replace("\n", " ").split('. ')
        elif filePath.endswith(".java"):
            lines = mark.read().split('\n')
        else:
            lines = mark.read().split('\n')
    for line in lines:
        # if filePath.endswith('README.md'): # formats README.md output, uncomment if needed
            # line = re.sub(r'(?s)(#)(.*?)(  )', '', line).strip()  # annoying
            # line, removes section headers from README.md files
        nextLine = list()
        if not line == '' and '#' not in line:  # removes unnecessary lines and headers
            nextLine.append(line)
            content.append(nextLine)
    return content  # list of lists
