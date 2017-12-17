# Not needed for this version, but could be used as a future enhancement
def write_to_default_file(stringToFile):
    f = open('default.txt', 'w')
    f.write(stringToFile)
    f.close()


# Writes the java statistics to a user-specified text file
def write_to_existing_file(stringToFile, FileName):
    f = open(FileName, 'w')
    f.write(stringToFile)
    f.close()
