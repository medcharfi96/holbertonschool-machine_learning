#!/usr/bin/env python3

""" task  3 and 2"""

import numpy as np


class MultiNormal:
    """representation dune distribution"""

    def __init__(self, data):
        """
        definition de la classe
        :param data:
        """
        if type(data) != np.ndarray:
            raise TypeError('data must be a 2D numpy.ndarray')
        if len(data.shape) != 2:
            raise TypeError("data must be a 2D numpy.ndarray")
        if (data.shape[1] < 2):
            raise ValueError("data must contain multiple data points")

        d = data.shape[0]
        n = data.shape[1]
        self.mean = np.mean(data, axis=1, keepdims=True)
        X = data - self.mean
        self.cov = np.dot(X, X.T) / (n - 1)
