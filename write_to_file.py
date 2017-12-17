# Not used in this feature, but could be used for a future enhancement
def write_to_default_file(stringToFile):
    f = open('default.txt', 'w')
    f.write(stringToFile)
    f.close()


# Writes java statistics to text file for use in other methods
def write_to_existing_file(stringToFile, FileName):
    f = open(FileName, 'w')
    f.write(stringToFile)
    f.close()
