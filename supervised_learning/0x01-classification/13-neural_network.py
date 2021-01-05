#!/usr/bin/env python3
"""
classe description
"""
import numpy as np


class NeuralNetwork():
    """
    classe neurone network
    """
    def __init__(self, nx, nodes):
        """
        constructeur parametré
        :param nx: int
        :param nodes: int
        """
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if type(nodes) is not int:
            raise TypeError("nodes must be an integer")
        if nodes < 1:
            raise ValueError("nodes must be a positive integer")
        self.__W1 = np.random.randn(nodes, nx)
        self.__b1 = np.zeros((nodes, 1))
        self.__A1 = 0
        self.__W2 = np.random.normal(size=(1, nodes))
        self.__b2 = 0
        self.__A2 = 0

    @property
    def W2(self):
        """
        get w2
        :return:
        """
        return self.__W2

    @property
    def b2(self):
        """
        get b2
        :return:
        """
        return self.__b2

    @property
    def A2(self):
        """
        get A2
        :return:
        """
        return self.__A2

    @property
    def W1(self):
        """
        get w1
        :return:
        """
        return self.__W1

    @property
    def b1(self):
        """
        get b1
        :return:
        """
        return self.__b1

    @property
    def A1(self):
        """
        get A1
        :return:
        """
        return self.__A1

    def forward_prop(self, X):
        """
        fonction de propagation
        :param X: ndarray
        :return:
        """
        v1 = np.matmul(self.__W1, X, None) + self.__b1
        res = 1 / (1 + np.exp(-v1))
        self.__A1 = res
        v2 = np.matmul(self.__W2, res, None) + self.__b2
        res2 = 1 / (1 + np.exp(-v2))
        self.__A2 = res2
        return (self.__A1, self.__A2)

    def cost(self, Y, A):
        """
        calcule le cout du lensemble de modele de regression
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

        A1, A2 = self.forward_prop(X)
        ras = np.round(A2)
        lal = self.cost(Y, A2)
        return (ras.astype(np.int), lal)

    def gradient_descent(self, X, Y, A1, A2, alpha=0.05):
        """
        calcule de gradient
        :param X: ndarray
        :param Y: ndarray
        :param A: ndarray
        :param alpha: taux dapprentissage
        :return:
        """
        m = len(X[0])
        dz2 = A2 - Y
        dw2 = np.matmul(dz2, A1.T) * 1 / m
        db2 = np.sum(dz2, axis=1, keepdims=True) * 1 / m
        dA1 = A1 * (1 - A1)
        dz1 = np.matmul(self.__W2.T, dz2) * dA1
        dw1 = np.matmul(dz1, X.T) * 1 / m
        db1 = np.sum(dz1, axis=1, keepdims=True) * 1 / m
        self.__W2 = self.__W2 - dw2 * alpha
        self.__b2 = self.__b2 - db2 * alpha
        self.__W1 = self.__W1 - dw1 * alpha
        self.__b1 = self.__b1 - db1 * alpha