def WriteToDefaultFile(stringToFile):
    f = open('default.txt', 'w')
    f.write(stringToFile)
    f.close()


def WriteToExistingFile(stringToFile, FileName):
    f = open(FileName, 'w')
    f.write(stringToFile)
    f.close()
