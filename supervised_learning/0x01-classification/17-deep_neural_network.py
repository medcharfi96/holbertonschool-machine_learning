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
            if layers[i] <= 0 or not isinstance(layers[i], int):
                raise TypeError("layers must be a list of positive integers")
            wb = "b" + str(i + 1)
            wK = "W" + str(i + 1)
            if i == 0:
                fr = np.sqrt(2 / nx)
                self.__weights[wK] = np.random.randn(layers[0], nx) * fr
                self.__weights[wb] = np.zeros((layers[0], 1))

            else:
                fr = np.sqrt(2 / layers[i - 1])
                self.__weights[wK] = np.random.randn(layers[i],
                                                     layers[i - 1]) * fr

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
