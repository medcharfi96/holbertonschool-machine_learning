#!/usr/bin/env python3
""" task 3 """


import numpy as np
kmeans = __import__('1-kmeans').kmeans
variance = __import__('2-variance').variance


def optimum_k(X, kmin=1, kmax=None, iterations=1000):
    """
    deduire le nombre optimal de cluster
    :param X:
    :param kmin:
    :param kmax:
    :param iterations:
    """
    if type(X) != np.ndarray or len(X.shape) != 2:
        return None, None

    if kmax is None:
        kmax = X.shape[0]

    if type(kmin) != int or kmin <= 0:
        return None, None

    if kmin >= X.shape[0]:
        return None, None

    if type(kmax) != int or kmax <= 0:
        return None, None

    if kmax > X.shape[0]:
        return None, None

    if kmin >= kmax:
        return None, None

    if type(iterations) != int or iterations <= 0:
        return None, None
    res = []
    vars = []
    c, cls = kmeans(X, kmin)
    var_min = variance(X, c)
    for i in range(kmin, kmax + 1):
        C, cls = kmeans(X, i)
        res.append((C, cls))
        varience = variance(X, C)
        vars.append(var_min - varience)
    return res, vars
