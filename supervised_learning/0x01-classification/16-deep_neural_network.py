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
        self.L = len(layers)
        self.cache = {}
        self.weights = {}
        for i in range(len(layers)):
            if (layers[i] <= 0) or not isinstance(layers[i], int):
                raise TypeError("layers must be a list of positive integers")
            wb = "b" + str(i+1)
            wK = "W" + str(i+1)
            if i > 0:
                fr = np.sqrt(2 / layers[i - 1])
                self.weights[wK] = np.random.randn(layers[i],
                                                   layers[i - 1]) * fr
            else:
                fr = np.sqrt(2 / nx)
                self.weights[wK] = np.random.randn(layers[0], nx) * fr
                self.weights[wb] = np.zeros((layers[0], 1))
