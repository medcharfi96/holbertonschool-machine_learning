#!/usr/bin/env python3
"""
task 1
"""

import numpy as np


def l2_reg_gradient_descent(Y, weights, cache, alpha, lambtha, L):
    """
    reg dec grad
    :param Y:
    :param weights:
    :param cache:
    :param alpha:
    :param lambtha:
    :param L:
    """
    m = Y.shape[1]
    der_z = cache['A' + str(L)]
    d_d_z = der_z - Y
    """w_cp = weights.copy()"""

    for j in range(L, 0, -1):
        k_b = 'b' + str(j)
        K_w = 'W' + str(j)
        klw = weights[K_w]
        k_ddz = cache['A' + str(j - 1)]
        w_cp = weights[K_w]
        der_b1 = (1 / m) * (np.sum(d_d_z, axis=1, keepdims=True))
        der_lt_w = (1 / m) * np.matmul(d_d_z, k_ddz.T) + ((lambtha / m) * klw)
        d_d_z = np.matmul(w_cp.T, d_d_z) * (1 - k_ddz * k_ddz)
        weights[K_w] = weights[K_w] - alpha * der_lt_w
        weights[k_b] = weights[k_b] - alpha * der_b1
