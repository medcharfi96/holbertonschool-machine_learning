#!/usr/bin/env python3
""" task 6 """


import numpy as np
pdf = __import__('5-pdf').pdf


def expectation(X, pi, m, S):
    """
    desc
    :param X:
    :param pi:
    :param m:
    :param S:
    :return:
    """
    if type(X) != np.ndarray or len(X.shape) != 2:
        return None
    if type(m) != np.ndarray or len(m.shape) != 1:
        return None
    if type(S) != np.ndarray or len(S.shape) != 2:
        return None
    if X.shape[1] != m.shape[0]:
        return None
    if X.shape[1] != S.shape[0] or X.shape[1] != S.shape[1]:
        return None
    if S.shape[0] != S.shape[1]:
        return None
    n, d = X.shape
    k = S.shape[0]
    tmp = np.zeros((k, n))

    for i in range(k):
        P = pdf(X, m[i], S[i])
        prior = pi[i]
        tmp[i] = prior * P

    g = tmp / np.sum(tmp, axis=0)
    likelihood = np.sum(np.log(np.sum(tmp, axis=0)))

    return g, likelihood
