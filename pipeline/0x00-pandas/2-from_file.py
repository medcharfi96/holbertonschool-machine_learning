#!/usr/bin/env python3
""" task 2 """
import pandas as pd


def from_file(filename, delimiter):
    """
    from  file
    :param filename:
    :param delimiter:
    """

    zeb = pd.read_csv(filename, sep=delimiter)
    return zeb
