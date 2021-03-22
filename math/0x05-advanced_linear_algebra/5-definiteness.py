#!/usr/bin/env python3
""" task 5 """

import numpy as np


def definiteness(matrix):
    """task 5"""

    if type(matrix) != np.ndarray:
        raise TypeError("matrix must be a numpy.ndarray")

    if len(matrix.shape) == 1:
        return None

    if not np.array_equal(matrix.T, matrix):
        return None

    eigenval = np.linalg.eigvals(matrix)

    if np.all(eigenval < 0):
        return "Negative definite"
    elif np.all(eigenval > 0):
        return "Positive definite"
    elif np.all(eigenval <= 0):
        return "Negative semi-definite"
    elif np.all(eigenval >= 0):
        return "Positive semi-definite"
    else:
        return "Indefinite"
