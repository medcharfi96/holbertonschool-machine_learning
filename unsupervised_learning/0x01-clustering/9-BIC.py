#!/usr/bin/env python3
""" task 9 """


import numpy as np
expectation_maximization = __import__('8-EM').expectation_maximization


def BIC(X, kmin=1, kmax=None, iterations=1000, tol=1e-5, verbose=False):
    """
    savoir le meilleur nbr
    :param X:
    :param kmin:
    :param kmax:
    :param iterations:
    :param tol:
    :param verbose:
    :return:
    """

    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        return None, None, None, None
    if type(kmin) != int or kmin <= 0 or kmin >= X.shape[0]:
        return None, None, None, None
    if type(kmax) != int or kmax <= 0 or kmax >= X.shape[0]:
        return None, None, None, None
    if kmin >= kmax:
        return None, None, None, None
    if type(iterations) != int or iterations <= 0:
        return None, None, None, None
    if type(tol) != float or tol <= 0:
        return None, None, None, None
    if type(verbose) != bool:
        return None, None, None, None

    n, d = X.shape
    k_r, result, l_b, b = [], [], [], []

    for k in range(kmin, kmax + 1):
        pi, m, S, g, like = expectation_maximization(
            X, k, iterations, tol, verbose)
        k_r.append(k)
        result.append((pi, m, S))
        l_b.append(like)
        p = (k * d * (d + 1) / 2) + (d * k) + k - 1
        bic = p * np.log(n) - 2 * like
        b.append(bic)
    b = np.array(b)
    best = np.argmin(b)
    l_b = np.array(l_b)

    return k_r[best], result[best], l_b[best], b[best]
