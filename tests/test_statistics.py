import statistics
import numpy as np
import collections

# def test_getStatistics():
#     """tests the getStatistics functions with a  median list numList list """
#     numList = [12, 25, 54, 23, 121, 235, 643, 234, 234, 432]
#     statString = statistics.get_statistics(numList)
#     correctStat = "min: 12 max: 643 mean: 201.3 StdDev: 194.537425705 iqr: 202.5 total: 2013"
#     assert statString == correctStat
#
#
#
# def test_getStatistics2():
#     """tests function with a small list"""
#     numList = [24, 10, 32, 55, 15, 40, 5]
#     statString = statistics.get_statistics(numList)
#     print("here", statString)
#     correctStat ="min: 5 max: 55 mean: 25.8571428571 StdDev: 16.4527771987 iqr: 23.5 total: 181"
#     assert statString == correctStat
#
#
#
# def test_getStatistics3():
#     """ test function with a big number list"""
#     numList = [516, 254, 21, 5, 24, 64, 75, 1000, 98, 41.4, 55.3, 14, 69, 150, 17, 365]
#     statString = statistics.get_statistics(numList)
#     correctStat = "min: 5.0 max: 1000.0 mean: 173.04375 StdDev: 254.678206195 iqr: 152.75 total: 2768.7"
#     assert statString == correctStat

def test_combine_statistics():
    dict = {"variables":[1,2,3,4], "classes":[1,1,2,1], "methods":[2,2,1,1], "lines": [21,55,10,65]}
    stat_string = statistics.combine_statistics(dict)
    stat_list = []
    for stat in stat_string.split("\n\n"):
        stat_list.append(stat.replace("\n",""))
    correctStat =["variablesmin: 1 max: 4 mean: 2.5 StdDev: 1.12 iqr: 1.5 total: 10","methodsmin: 1 max: 2 mean: 1.5 StdDev: 0.5 iqr: 1.0 total: 6", "linesmin: 10 max: 65 mean: 37.75 StdDev: 22.86 iqr: 39.25 total: 151", "classesmin: 1 max: 2 mean: 1.25 StdDev: 0.43 iqr: 0.25 total: 5"]

    assert collections.Counter(stat_list) == collections.Counter(correctStat)
