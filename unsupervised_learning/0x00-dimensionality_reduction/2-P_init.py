#!/usr/bin/env python3
""" task 2"""


import numpy as np


def P_init(X, perplexity):
    """
    p init
    :param X:
    :param perplexity:
    """
    n, d = X.shape
    EX = np.sum(np.square(X), axis=1)
    D = (np.add(np.add(-2 * np.dot(X, X.T), EX).T, EX))
    np.fill_diagonal(D, 0)
    P = np.zeros((n, n))
    betas = np.ones([n, 1], dtype='float64')
    H = np.log2(perplexity)

    return (D, P, betas, H)
