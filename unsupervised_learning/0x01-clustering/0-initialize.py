#!/usr/bin/env python3
""" tassk 0 """


import numpy as np


def initialize(X, k):
    """
    inisialisation de cluster
    :param X:
    :param k:
    """
    n, d = X.shape
    if type(k) is not int or k <= 0:
        return None
    min = X.min(axis=0)
    max = X.max(axis=0)
    point = np.random.uniform(low=min, high=max, size=(k, d))
    return point
