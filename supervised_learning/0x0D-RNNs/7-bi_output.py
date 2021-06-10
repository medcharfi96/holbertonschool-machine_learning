#!/usr/bin/env python3
""" task 7 """


import numpy as np


def softmax(x):
    """
    softmax fn
    :param x:
    :return:
    """
    return np.exp(x) / np.sum(np.exp(x), axis=1, keepdims=True)


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
        calcule detat cache adns la prop
        :param h_prev:
        :param x_t:
        :return:
        """

        h_x = np.concatenate((h_prev, x_t), axis=1)
        h_next = np.tanh(np.matmul(h_x, self.Whf) + self.bhf)

        return h_next

    def backward(self, h_next, x_t):
        """
        calcu detat cahce dans la repropagation
        :param h_next:
        :param x_t:
        :return:
        """

        h_x = np.concatenate((h_next, x_t), axis=1)
        h_prev = np.tanh(np.matmul(h_x, self.Whb) + self.bhb)

        return h_prev

    def output(self, H):
        """
        calcule des sorties
        :param H:
        :return:
        """

        t = H.shape[0]
        Y = []

        for time in range(t):
            y = np.matmul(H[time], self.Wy) + self.by
            y = softmax(y)
            Y.append(y)

        return np.array(Y)
