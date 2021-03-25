#!/usr/bin/env python3
""" task 1 """


import numpy as np


def intersection(x, n, P, Pr):
    """
    ras zebi fil  brouklou
    :param x:
    :param n:
    :param P:
    :param Pr:
    """
    if type(n) is not int or (n <= 0):
        raise ValueError('n must be a positive integer')

    if type(x)is not int or (x < 0):
        erreur = 'x must be an integer that is greater than or equal to 0'
        raise ValueError(erreur)

    if x > n:
        raise ValueError('x cannot be greater than n')

    if type(P) != np.ndarray or len(P.shape) != 1:
        raise TypeError('P must be a 1D numpy.ndarray')
    if type(Pr) != np.ndarray or len(Pr.shape) != 1:
        raise TypeError('P must be a 1D numpy.ndarray')

    for item in P:
        if item > 1 or item < 0:
            raise ValueError('All values in P must be in the range [0, 1]')
    for item in Pr:
        if item > 1 or item < 0:
            raise ValueError('All values in P must be in the range [0, 1]')

    test = np.sum(Pr)
    if not np.isclose(test, 1):
        raise ValueError("Pr must sum to 1")

    fact = np.math.factorial(n) / (np.math.factorial(x)
                                   * np.math.factorial(n - x))
    total = fact * (P ** x) * (np.power((1 - P), (n - x)))
    ret = total * Pr
    return ret
