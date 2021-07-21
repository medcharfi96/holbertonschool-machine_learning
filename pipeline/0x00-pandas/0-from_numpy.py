#!/usr/bin/env python3
import pandas as pd
""" task 0 """


def from_numpy(array):
    """
    from numpy
    :param array:
    """

    text = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    if array.shape[1] > 26:
        df = pd.DataFrame(array)
        df = df.iloc[:, 0:26]
        df.columns = text

    else:
        col = text[:array.shape[1]]
        df = pd.DataFrame(array, columns=col)

    return df
