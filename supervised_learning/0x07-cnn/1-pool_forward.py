#!/usr/bin/env python3
""" task 1"""
import numpy as np


def pool_forward(A_prev, kernel_shape, stride=(1, 1), mode='max'):
    """
    desc
    :param A_prev:
    :param W:
    :param b:
    :param activation:
    :param padding:
    :param stride:
    :return:
    """
    m_prev = A_prev.shape[0]
    h_prev = A_prev.shape[1]
    w_prev = A_prev.shape[2]
    c_prev = A_prev.shape[3]
    h_krnl = kernel_shape[0]
    w_krnl = kernel_shape[1]
    str_h, str_w = stride

    final_h = int(((h_prev - h_krnl) / str_h) + 1)
    final_w = int(((w_prev - w_krnl) / str_w) + 1)
    H = np.zeros((m_prev, final_h, final_w, c_prev))

    for i in range(final_h):
        for j in range(final_w):
            if mode == 'max':
                H[:, i, j] = np.max(A_prev[:,
                                    i * str_h:(h_krnl + (i * str_h)),
                                    j * str_w:(w_krnl + (j * str_w))],
                                    axis=(1, 2))
            else:
                H[:, i, j] = np.mean(A_prev[:,
                                     i * str_h:(h_krnl + (i * str_h)),
                                     j * str_w:(w_krnl + (j * str_w))],
                                     axis=(1, 2))
    return H
