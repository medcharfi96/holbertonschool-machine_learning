#!/usr/bin/env python3
""" task 2 """


import numpy as np


def variance(X, C):
    """
    calcule de intra-cluster variance
    :param X:
    :param C:
    """
    if type(X) != np.ndarray or len(X.shape) != 2:
        return None
    if type(C) != np.ndarray or len(C.shape) != 2:
        return None
    if X.shape[1] != C.shape[1]:
        return None

    n, d = X.shape
    k, d1 = C.shape

    distance = np.sqrt(((X - C[:, np.newaxis])**2).sum(axis=-1))
    mini = np.min(distance, axis=0)
    var = np.sum(np.square(mini))
    return var
