#!/usr/bin/env python3
""" task 1 """


import numpy as np


def regular(P):
    """
    etat stationnaire
    :param P:
    """

    if type(P) != np.ndarray:
        return None
    n, k = P.shape
    s = np.ones((1, n)) / k
    boul = True

    s = np.matmul(s, P)
    for i in range(n):
        if np.any(P[i]) <= 0:
            return None
    while(boul):
        s_prec = s
        s = np.matmul(s, P)
        if np.all(s == s_prec):
            return s
