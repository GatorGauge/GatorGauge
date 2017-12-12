""" statistical functions """

import numpy as np


def get_statistics(numerical_list):
    """ calculate various basic statistics """
    q75, q25 = np.percentile(numerical_list, [75, 25])
    iqr = q75 - q25
    stat_string = "min: " + \
        str(np.min(numerical_list)) + " max: " + \
        str(np.max(numerical_list)) + " mean: " + \
        str(np.mean(numerical_list)) + " StdDev: " + \
        str(np.std(numerical_list)) + " iqr: " + str(iqr)
    return stat_string


def print_statistics(dictionary):
    """ pretty-print statistics dictionary """
    for key, values in dictionary.items():
        print(key + "\n" + get_statistics(values))
