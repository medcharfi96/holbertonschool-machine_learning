#!/usr/bin/env python3
"""task 8 """


import numpy as np
initialize = __import__('4-initialize').initialize
expectation = __import__('6-expectation').expectation
maximization = __import__('7-maximization').maximization


def expectation_maximization(X, k, iterations=1000, tol=1e-5, verbose=False):
    """
    description
    :param X:
    :param k:
    :param iterations:
    :param tol:
    :param verbose:
    :return:
    """

    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        return None, None, None, None, None
    if type(k) != int or k <= 0 or k >= X.shape[0]:
        return None, None, None, None, None
    if type(iterations) != int or iterations <= 0:
        return None, None, None, None, None
    if type(tol) != float or tol <= 0:
        return None, None, None, None, None
    if type(verbose) != bool:
        return None, None, None, None, None

    pi, m, S = initialize(X, k)
    prev_like = 0
    g, likelihood = expectation(X, pi, m, S)

    for i in range(iterations):
        if verbose and (i % 10 == 0):
            msg = 'Log Likelihood after {} iterations: {}'\
                .format(i, likelihood.round(5))
            print(msg)
        pi, m, S = maximization(X, g)
        g, likelihood = expectation(X, pi, m, S)

        if abs(likelihood - prev_like) <= tol:
            break
        prev_like = likelihood

    if verbose:
        msg = 'Log Likelihood after {} iterations: {}'\
            .format(i + 1, likelihood.round(5))
        print(msg)

    return pi, m, S, g, likelihood
