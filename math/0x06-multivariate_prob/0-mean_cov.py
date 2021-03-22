#!/usr/bin/env python3
""" task 0 """

import numpy as np


def mean_cov(X):
    """
    get the mean
    :param X:
    """

    if type(X) != np.ndarray:
        raise TypeError('X must be a 2D numpy.ndarray')
    if len(X.shape) != 2:
        raise TypeError('X must be a 2D numpy.ndarray')
    if (X.shape[0] < 2):
        raise ValueError("X must contain multiple data points")

    moyenne = X.mean(axis=0)
    moyenne = np.reshape(moyenne, (1, X.shape[1]))

    x = X - moyenne
    cov = np.dot(x.T, x) / (X.shape[0] - 1)
    return moyenne, cov
