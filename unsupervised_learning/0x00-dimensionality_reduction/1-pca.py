#!/usr/bin/env python3
""" task 1 """


import numpy as np


def pca(X, ndim):
    """
    pca
    :param X:
    :param ndim:
    """
    X = X - np.mean(X, axis=0)
    Vh = np.linalg.svd(X)[2]
    W = Vh[:ndim].T
    return np.matmul(X, W)
