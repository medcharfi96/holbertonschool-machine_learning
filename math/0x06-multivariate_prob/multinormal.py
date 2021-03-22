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

    def pdf(self, x):
        """
        calcule pdf
        :param x:
        """
        d = self.cov.shape[0]
        if type(x) != np.ndarray:
            raise TypeError('x must be a numpy.ndarray')

        if (len(x.shape) != 2) or (x.shape[1] != 1) or (x.shape[0] != d):
            raise ValueError("x must have the shape ({}, 1)".format(d))
        Xmax = x - self.mean
        M = np.sqrt((2 * np.pi) ** d * np.linalg.det(self.cov))
        K = np.exp(-(np.linalg.solve(self.cov, Xmax).T.dot(Xmax)) * 0.5)
        pdf_retour = (1 / (M) * K)
        return pdf_retour[0][0]
