def write_to_default_file(stringToFile):
    f = open('default.txt', 'w')
    f.write(stringToFile)
    f.close()


def write_to_existing_file(stringToFile, FileName):
    f = open(FileName, 'w')
    f.write(stringToFile)
    f.close()
