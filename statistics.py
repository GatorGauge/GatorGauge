import numpy as np


def getStatistics(numericalList):
    q75, q25 = np.percentile(numericalList, [75, 25])
    iqr = q75 - q25
    statString = "min: " + str(np.min(numericalList)) + " max: " \
        + str(np.max(numericalList)) + " mean: " + str(np.mean(numericalList)) \
        + " StdDev: " + str(np.std(numericalList)) + " iqr: " + str(iqr)
    return statString


def printStatistics(dictionary):
    for key, values in dictionary.items():
        print(key + "\n" + getStatistics(values))
