#!/usr/bin/env python3
""" task 0 """


import numpy as np


class RNNCell():
    """ class description """
    def __init__(self, i, h, o):
        """
        constructeur
        :param i:
        :param h:
        :param o:
        """

        self.Wh = np.random.normal(size=(h + i, h))
        self.Wy = np.random.normal(size=(h, o))
        self.bh = np.zeros((1, h))
        self.by = np.zeros((1, o))

    def softmax(self, x):
        """
        fonction de calcule de softmax
        :param x:
        :return:
        """

        x_max = np.max(x, axis=1, keepdims=True)
        e_x = np.exp(x - x_max)

        return e_x / np.sum(e_x, axis=1, keepdims=True)

    def forward(self, h_prev, x_t):
        """
        forward propagation
        :param h_prev:
        :param x_t:
        :return:
        """

        h_x = np.concatenate((h_prev, x_t), axis=1)
        h_next = np.tanh(np.matmul(h_x, self.Wh) + self.bh)
        y = np.matmul(h_next, self.Wy) + self.by
        y = self.softmax(y)

        return h_next, y
