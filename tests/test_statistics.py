import statistics
import numpy as np

def test_getStatistics):
    """tests the getStatistics functions with a numList list """
    numList = [12, 25, 54, 23, 121, 235, 643, 234, 234, 432]
    statString = statistics.getStatistics(numList)
    correctStat = "min: 12 max: 643 mean: 201.3 StdDev: 194.537425705 iqr: 202.5"
    assert statString == correctStat
