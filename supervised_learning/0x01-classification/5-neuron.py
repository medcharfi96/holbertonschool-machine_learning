#!/usr/bin/env python3
"""
classe neurone
"""


import numpy as np


class Neuron():
    """
    description de classe
    """
    def __init__(self, nx):
        """
        constructeur parametré
        :param nx: int
        """
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        self.nx = nx
        self.__W = np.random.randn(1, nx)
        self.__A = 0
        self.__b = 0

    @property
    def W(self):
        """
         Getter W
        :return:
        """
        return self.__W

    @property
    def A(self):
        """
        Getter A
        """
        return self.__A

    @property
    def b(self):
        """
        Getter b
        :return:
        """
        return self.__b

    def forward_prop(self, X):
        """
        propagation avant du neurone
        :param X: int
        :return:
        """
        v = np.matmul(self.__W, X, None) + self.__b
        res = 1 / (1 + np.exp(-v))
        self.__A = res
        return self.__A

    def cost(self, Y, A):
        """
        calcule le cout du modele de regression
        :param Y: ndarray
        :param A: ndarray  represent y chapeau
        :return:
        """
        m = Y.shape[1]
        za = 1.0000001 - A
        cost = (np.sum(Y * np.log(A) + (1 - Y) * np.log(za)))/m
        return (-1 * cost)

    def evaluate(self, X, Y):
        """
        eval de prediction
        :param X: ndarray
        :param Y: ndarray
        :return:
        """

        z = self.forward_prop(X)
        ras = np.round(z)
        lal = self.cost(Y, z)
        return (ras.astype(np.int), lal)

    def gradient_descent(self, X, Y, A, alpha=0.05):
        """
        calcule de gradient
        :param X: ndarray
        :param Y: ndarray
        :param A: ndarray
        :param alpha: taux dapprentissage
        :return:
        """
        m = Y.shape[1]
        db = np.sum(A-Y) / m
        dW = np.sum(np.matmul(X, (A - Y).T, None))/m
        self.__W = self.__W - alpha * dW.T
        self.__b = self.__b - alpha * db