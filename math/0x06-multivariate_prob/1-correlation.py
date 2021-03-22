#!/usr/bin/env python3
""" task 1 """

import numpy as np


def correlation(C):
    """
    desc
    :param C:
    """
    if type(C) != np.ndarray:
        raise TypeError('C must be a numpy.ndarray')

    if len(C.shape) != 2:
        raise ValueError("C must be a 2D square matrix")

    if (C.shape[0] != C.shape[1]):
        raise ValueError("C must be a 2D square matrix")

    variance = np.sqrt(np.diag(C))
    cor = 1 / (np.outer(variance, variance) / C)
    return cor
