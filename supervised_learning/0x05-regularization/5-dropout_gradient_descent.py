#!/usr/bin/env python3
""" task 5"""
import numpy as np


def dropout_gradient_descent(Y, weights, cache, alpha, keep_prob, L):
    """

    :param Y:
    :param weights:
    :param cache:
    :param alpha:
    :param keep_prob:
    :param L:
    """
    m = Y.shape[1]
    ZZ = cache["A"+str(L)] - Y
    for i in range(L, 0, -1):
        BB = "b"+str(i)

        WW = "W"+str(i)
        AA = "A"+str(i-1)

        CA = cache[AA]
        dw = ((1/m) * np.matmul(ZZ, CA.T))
        db = (1/m) * np.sum(ZZ, axis=1, keepdims=True)

        zeb = 1 - np.power(CA, 2)
        if i > 1:
            ZZ = ZZ.T * zeb
            ZZ = ZZ / keep_prob
        else:
            ZZ = cache["A"+str(L)] - Y
        weights[WW] = weights[WW] - dw * alpha
        weights[BB] = weights[BB] - db * alpha
