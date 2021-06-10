#!/usr/bin/env python3
""" task 1 """


import numpy as np


def rnn(rnn_cell, X, h_0):
    """
    performer la propagation
    :param rnn_cell:
    :param X:
    :param h_0:
    :return:
    """

    t, m, i = X.shape
    _, h = h_0.shape

    Y = []
    H = np.zeros((t + 1, m, h))
    H[0, :, :] = h_0
    for step in range(t):
        h, y = rnn_cell.forward(H[step], X[step])
        H[step + 1, :, :] = h
        Y.append(y)
    Y = np.asarray(Y)
    return H, Y
