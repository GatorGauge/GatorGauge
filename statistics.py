""" statistical functions """

import numpy as np


def get_statistics(numerical_list):
    """ calculate various basic statistics """
    q75, q25 = np.percentile(numerical_list, [75, 25])
    iqr = q75 - q25
    stat_string = "min: " + \
        str(np.min(numerical_list)) + " max: " + \
        str(round(np.max(numerical_list), 2)) + " mean: " + \
        str(round(np.mean(numerical_list), 2)) + " StdDev: " + \
        str(round(np.std(numerical_list), 2)) + " iqr: " + \
        str(iqr) + " total: " + str(np.sum(numerical_list))
    return stat_string


def combine_statistics(dictionary):
    """ pretty-print statistics dictionary """
    stat_string = ""
    for key, values in dictionary.items():
        curr_stat = key + "\n" + get_statistics(values)
        stat_string = stat_string + "\n" + curr_stat + "\n"
    return stat_string
