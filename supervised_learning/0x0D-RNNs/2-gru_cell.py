#!/usr/bin/env python3
""" task 2 """


import numpy as np


def sigmoid(x):
    """
    fonctionde sig
    :param x:
    :return:
    """
    sigmoid = 1 / (1 + np.exp(-x))
    return sigmoid


class GRUCell():
    """ classe decription"""

    def __init__(self, i, h, o):
        """
        constructeur
        :param i:
        :param h:
        :param o:
        """
        self.Wz = np.random.normal(size=(h + i, h))
        self.Wr = np.random.normal(size=(h + i, h))
        self.Wh = np.random.normal(size=(h + i, h))
        self.Wy = np.random.normal(size=(h, o))
        # Bias
        self.bz = np.zeros((1, h))
        self.br = np.zeros((1, h))
        self.bh = np.zeros((1, h))
        self.by = np.zeros((1, o))

    def softmax(self, x):
        """
        fonction de calc de softmax
        :param x:
        :return:
        """

        x_max = np.max(x, axis=1, keepdims=True)
        e_x = np.exp(x - x_max)

        return e_x / np.sum(e_x, axis=1, keepdims=True)

    def forward(self, h_prev, x_t):
        """
        performer la forward prop
        :param h_prev:
        :param x_t:
        :return:
        """

        matrix = np.concatenate((h_prev, x_t), axis=1)
        z_t = sigmoid(np.matmul(matrix, self.Wz) + self.bz)
        r_t = sigmoid(np.matmul(matrix, self.Wr) + self.br)

        matrix2 = np.concatenate((r_t * h_prev, x_t), axis=1)
        prime_h = np.tanh(np.matmul(matrix2, self.Wh) + self.bh)

        h_next = (1 - z_t) * h_prev + z_t * prime_h
        y = self.softmax(np.matmul(h_next, self.Wy) + self.by)

        return h_next, y
