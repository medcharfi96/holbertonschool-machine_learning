#!/usr/bin/env python3
"""
class desc
"""


import numpy as np


class DeepNeuralNetwork:
    """
    class desc
    """

    def __init__(self, nx, layers):
        """class desc"""
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if not isinstance(layers, list) or len(layers) == 0:
            raise TypeError("layers must be a list of positive integers")
        self.__L = len(layers)
        self.__cache = {}
        self.__weights = {}
        for i in range(len(layers)):
            if not isinstance(layers[i], int) or layers[i] <= 0:
                raise TypeError("layers must be a list of positive integers")

            if i > 0:
                self.__weights['W' + str(i + 1)] = \
                    np.random.randn(layers[i], layers[i - 1]) * \
                    np.sqrt(2 / layers[i - 1])
            else:
                v = np.sqrt(2 / nx)
                self.__weights['W' + str(i + 1)
                               ] = np.random.randn(layers[0], nx) * v
            self.__weights['b' + str(i + 1)] = np.zeros((layers[i], 1))

    @property
    def L(self):
        """des"""
        return self.__L

    @property
    def cache(self):
        """desc"""
        return self.__cache

    @property
    def weights(self):
        """desc"""
        return self.__weights
