#!/usr/bin/env python3
""" task 4 """


import numpy as np
kmeans = __import__('1-kmeans').kmeans


def initialize(X, k):
    """
    initialisation de variable de gaussian
    :param X:
    :param k:
    """

    if type(X) != np.ndarray or len(X.shape) != 2:
        return None, None, None

    if type(k) != int or k <= 0:
        return None, None, None

    n, d = X.shape
    pi = np.tile(1/k, (k))
    c, clss = kmeans(X, k)
    S = np.tile(np.identity(d), (k))
    S = S.reshape(k, d, d)

    return pi, c, S
