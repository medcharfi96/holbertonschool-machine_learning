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
