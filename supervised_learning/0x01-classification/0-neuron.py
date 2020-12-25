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
        self.W = np.random.randn(1, nx)
        self.A = 0
        self.b = 0
