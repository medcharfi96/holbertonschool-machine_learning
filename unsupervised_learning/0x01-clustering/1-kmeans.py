#!/usr/bin/env python3
""" task 1 """


import numpy as np


def kmeans(X, k, iterations=1000):
    """
    faire le test des kmeans
    :param X:
    :param k:
    :param iterations:
    """
    if type(X) is not np.ndarray or len(X.shape) != 2:
        return None, None
    if type(k) is not int or k <= 0:
        return None, None
    n, d = X.shape
    if n < k:
        return None, None
    C = initialize(X, k)
    ancien = np.ndarray.copy(C)
    for i in range(iterations):
        delta = X - C[:, np.newaxis]
        dsit = np.sqrt((delta ** 2).sum(axis=2))
        clss = np.argmin(dsit, axis=0)
        for j in range(k):
            if len(X[clss == j]) == 0:
                C[j] = initialize(X, 1)
            else:
                C[j] = np.mean(X[clss == j], axis=0)
        delta = X - C[:, np.newaxis]
        dsit = np.sqrt((delta ** 2).sum(axis=2))
        clss = np.argmin(dsit, axis=0)
        if np.all(C == ancien):
            return C, clss
    return C, clss


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
