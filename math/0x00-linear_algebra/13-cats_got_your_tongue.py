#!/usr/bin/env python3
""" concatination """
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """ desc """
    return np.concatenate((mat1, mat2), axis)
