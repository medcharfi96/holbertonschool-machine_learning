#!/usr/bin/env python3
""" task 0 """


import numpy as np


def likelihood(x, n, P):
    """
    calcule de likelihood
    :param x:
    :param n:
    :param P:
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

    for item in P:
        if item > 1 or item < 0:
            raise ValueError('All values in P must be in the range [0, 1]')

    fact = np.math.factorial(n) / (np.math.factorial(x)
                                   * np.math.factorial(n - x))
    total = fact * (P ** x) * (np.power((1 - P), (n - x)))

    return total
