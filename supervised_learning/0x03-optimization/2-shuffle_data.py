#!/usr/bin/env python3
"""
task 2
"""
import numpy as np


def shuffle_data(X, Y):
    """mélange les points de données dans deux matrices de la même manière"""
    mel = np.random.permutation(len(X))
    return X[mel], Y[mel]
