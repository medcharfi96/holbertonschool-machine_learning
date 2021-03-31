#!/usr/bin/env python3
""" tassk 0 """


import numpy as np


def initialize(X, k):
    """
    inisialisation de cluster
    :param X:
    :param k:
    """
    if type(X) != np.ndarray or len(X.shape) != 2:
        return None
    if type(k) is not int or k <= 0:
        return None
    n, d = X.shape

    min = X.min(axis=0)
    max = X.max(axis=0)
    point = np.random.uniform(low=min, high=max, size=(k, d))
    return point
