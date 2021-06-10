#!/usr/bin/env python3
""" task 6 """


import numpy as np


class BidirectionalCell():
    """ class desc"""

    def __init__(self, i, h, o):
        """
        constructeur
        :param i:
        :param h:
        :param o:
        """

        self.Whf = np.random.normal(size=(h + i, h))
        self.Whb = np.random.normal(size=(h + i, h))
        self.Wy = np.random.normal(size=(2 * h, o))
        self.bhf = np.zeros((1, h))
        self.bhb = np.zeros((1, h))
        self.by = np.zeros((1, o))

    def forward(self, h_prev, x_t):
        """
        calcule etat caché
        :param h_prev:
        :param x_t:
        :return:
        """

        h_x = np.concatenate((h_prev, x_t), axis=1)
        h_next = np.tanh(np.matmul(h_x, self.Whf) + self.bhf)

        return h_next

    def backward(self, h_next, x_t):
        """
        calcule detat cache
        :param h_next:
        :param x_t:
        :return:
        """

        h_x = np.concatenate((h_next, x_t), axis=1)
        h_prev = np.tanh(np.matmul(h_x, self.Whb) + self.bhb)

        return h_prev
