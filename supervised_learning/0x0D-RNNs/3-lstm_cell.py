#!/usr/bin/env python3
""" task 3 """


import numpy as np


def sigmoid(x):
    """
    sigmoide fn
    :param x:
    :return:
    """
    sigmoid = 1 / (1 + np.exp(-x))
    return sigmoid


class LSTMCell():
    """ class  description"""

    def __init__(self, i, h, o):
        """
        constructeur
        :param i:
        :param h:
        :param o:
        """

        self.Wf = np.random.normal(size=(h + i, h))
        self.Wu = np.random.normal(size=(h + i, h))
        self.Wc = np.random.normal(size=(h + i, h))
        self.Wo = np.random.normal(size=(h + i, h))
        self.Wy = np.random.normal(size=(h, o))
        self.bf = np.zeros((1, h))
        self.bu = np.zeros((1, h))
        self.bc = np.zeros((1, h))
        self.bo = np.zeros((1, h))
        self.by = np.zeros((1, o))

    def softmax(self, x):
        """
        softmax fn
        :param x:
        :return:
        """

        x_max = np.max(x, axis=1, keepdims=True)
        e_x = np.exp(x - x_max)

        return e_x / np.sum(e_x, axis=1, keepdims=True)

    def forward(self, h_prev, c_prev, x_t):
        """
        amiliorer la prop
        :param h_prev:
        :param c_prev:
        :param x_t:
        :return:
        """

        matrix = np.concatenate((h_prev, x_t), axis=1)
        u_t = sigmoid(np.matmul(matrix, self.Wu) + self.bu)
        f_t = sigmoid(np.matmul(matrix, self.Wf) + self.bf)
        o_t = sigmoid(np.matmul(matrix, self.Wo) + self.bo)

        prime_c = np.tanh(np.matmul(matrix, self.Wc) + self.bc)
        c_next = f_t * c_prev + u_t * prime_c
        h_next = o_t * np.tanh(c_next)

        y = self.softmax(np.matmul(h_next, self.Wy) + self.by)

        return h_next, c_next, y
