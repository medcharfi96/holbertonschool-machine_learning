#!/usr/bin/env python3
""" task 5"""


import numpy as np


def pdf(X, m, S):
    """
    pdf
    :param X:
    :param m:
    :param S:
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
    x_m = X - m
    S_inv = np.linalg.inv(S)

    fac = np.einsum('...k,kl,...l->...', x_m, S_inv, x_m)
    P1 = 1. / (np.sqrt(((2 * np.pi) ** d * np.linalg.det(S))))
    P2 = np.exp(-fac / 2)
    P = np.maximum((P1 * P2), 1e-300)

    return P
