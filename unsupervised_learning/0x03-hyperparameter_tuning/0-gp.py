#!/usr/bin/env python3
""" task 0"""


import numpy as np


class GaussianProcess():
    """ classe description """

    def __init__(self, X_init, Y_init, l=1, sigma_f=1):
        """
        constructeur
        :param X_init:
        :param Y_init:
        :param l:
        :param sigma_f:
        """
        self.X = X_init
        self.Y = Y_init
        self.l = l
        self.sigma_f = sigma_f
        self.K = self.kernel(X_init, X_init)

    def kernel(self, X1, X2):
        """
        calcule de covariance
        :param X1:
        :param X2:
        """
        somme = np.sum(X1 ** 2, 1).reshape(-1, 1) + np.sum(X2 ** 2, 1)
        retrait = somme + (-2 * np.dot(X1, X2.T))
        final = self.sigma_f ** 2 * np.exp(-0.5 / self.l ** 2 * retrait)
        return final
