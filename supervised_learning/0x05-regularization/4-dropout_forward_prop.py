#!/usr/bin/env python3
""" task 4"""
import numpy as np


def dropout_forward_prop(X, weights, L, keep_prob):
    """
    descr
    :param X:
    :param weights:
    :param L:
    :param keep_prob:
    :return:
    """
    cache = {}
    cache['A0'] = X
    for count in range(0, L):
        K_A = 'A' + str(count)
        K_W = 'W' + str(count + 1)
        Al = cache[K_A]
        Ca_w = weights[K_W]
        ca_b = weights['b' + str(count + 1)]
        Z = np.matmul(Ca_w, Al) + ca_b
        if count == L - 1:
            aasba = np.exp(Z)
            va = aasba / aasba.sum(axis=0, keepdims=True)
            cache['A' + str(count + 1)] = va
        else:
            aasba = (2 / (1 + np.exp(-2 * Z))) - 1
            FN_bin = np.random.binomial(1, keep_prob, (aasba.shape[0],
                                                       aasba.shape[1]))
            aasba = FN_bin * aasba
            cache['D' + str(count + 1)] = FN_bin
            cache['A' + str(count + 1)] = aasba / keep_prob
    return cache
