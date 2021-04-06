#!/usr/bin/env python3
""" task 1 """


import numpy as np


def markov_chain(P, s, t=1):
    """
    proba de markov chaine
    :param P:
    :param s:
    :param t:
    """

    if type(P) != np.ndarray:
        return None
    if type(t) is not int or t < 0:
        return None

    for i in range(0, t):
        s = np.matmul(s, P)

    return s
