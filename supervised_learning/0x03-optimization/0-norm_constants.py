#!/usr/bin/env python3
""" ta """

import numpy as np


def normalization_constants(X):
    """
    calcule de la normalisation moyenne dun matrice
    :param X: matrix
    :return:
    """
    mn = np.mean(X, axis=0)
    std1 = np.std(X, axis=0)
    return (mn, std1)
