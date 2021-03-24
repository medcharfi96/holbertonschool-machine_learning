#!/usr/bin/env python3
""" task 0 """


import numpy as np


def pca(X, var=0.95):
    """
    calculate pca
    :param X:
    :param var:
    """
    U = np.linalg.svd(X)[0]
    s = np.linalg.svd(X)[1]
    vh = np.linalg.svd(X)[2]
    variance = np.cumsum(s, dtype=None) / np.sum(s)

    result = np.argwhere(variance >= var)[0, 0]
    result = result + 1
    W = vh[: result].T
    return W
