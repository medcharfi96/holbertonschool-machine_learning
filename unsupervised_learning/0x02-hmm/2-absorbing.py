#!/usr/bin/env python3
""" task 2 """


import numpy as np


def absorbing(P):
    """
    verification si la chaine est absorbante
    :param P:
    """

    if type(P) != np.ndarray:
        return None

    d = np.diag(P)
    if (d == 1).all():
        return True

    if not(d == 1).any():
        return False

    if (d == 1).any():
        for i in range(P.shape[0]):
            for j in range(P.shape[0]):
                if i == j and i + 1 < len(P):
                    if P[i + 1][j] == 0 and P[i][j + 1] == 0:
                        return False
    return True
