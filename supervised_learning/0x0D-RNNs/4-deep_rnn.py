#!/usr/bin/env python3
""" task 4"""


import numpy as np


def deep_rnn(rnn_cells, X, h_0):
    """
    performer la prop
    :param rnn_cells:
    :param X:
    :param h_0:
    :return:
    """

    t_layers = len(rnn_cells)
    t, m, i = X.shape
    _, _, h_ = h_0.shape

    H = np.zeros((t + 1, t_layers, m, h_))
    H[0] = h_0

    for time in range(t):
        for layer in range(t_layers):
            if layer == 0:
                h, y = rnn_cells[layer].forward(H[time, layer], X[time])
            else:
                h, y = rnn_cells[layer].forward(H[time, layer], h)

            H[time + 1, layer, ...] = h

            if layer == t_layers - 1:
                if time == 0:
                    Y = y
                else:
                    Y = np.concatenate((Y, y))

    Y = Y.reshape(t, m, Y.shape[-1])

    return H, Y
