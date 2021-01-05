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
