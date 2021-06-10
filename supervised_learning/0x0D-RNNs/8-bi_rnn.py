#!/usr/bin/env python3
""" task 8 """


import numpy as np


def bi_rnn(bi_cell, X, h_0, h_t):
    """
    desc
    :param bi_cell:
    :param X:
    :param h_0:
    :param h_t:
    :return:
    """
    t, m, i = X.shape
    _, h = h_0.shape
    H_f = np.zeros((t + 1, m, h))
    H_b = np.zeros((t + 1, m, h))
    H_f[0] = h_0
    H_b[t] = h_t

    for t_i in range(t):
        H_f[t_i + 1] = bi_cell.forward(H_f[t_i], X[t_i])

    for t_j in range(t - 1, -1, -1):
        H_b[t_j] = bi_cell.backward(H_b[t_j + 1], X[t_j])

    H = np.concatenate((H_f[1:], H_b[0:t]), axis=2)
    Y = bi_cell.output(H)
    return H, Y
