#!/usr/bin/env python3
""" task 0"""
import numpy as np


def conv_forward(A_prev, W, b, activation, padding="same", stride=(1, 1)):
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
    h_krnl = W.shape[0]
    w_krnl = W.shape[1]
    c_krnl = W.shape[2]
    nc_krnl = W.shape[3]
    str_h, str_w = stride
    if padding == "same":
        ph = int(((h_prev - 1) * str_h + h_krnl - h_prev) / 2) + \
             (h_krnl % 2 == 0)
        pw = int(((w_prev - 1) * str_w + w_krnl - w_prev) / 2) + \
             (w_krnl % 2 == 0)
    if padding == "valid":
        ph = 0
        pw = 0
    final_h = int(((h_prev - h_krnl + (2 * ph)) / str_h) + 1)
    final_w = int(((w_prev - w_krnl + (2 * pw)) / str_w) + 1)
    img = np.pad(A_prev, ((0, 0), (ph, ph), (pw, pw), (0, 0)), mode='constant')
    H = np.zeros((m_prev, final_h, final_w, c_prev))
    for i in range(final_h):
        for j in range(final_w):
            for re in range(c_krnl):
                H[:, i, j, re] = np.sum(np.multiply(img[:,
                                                    i*str_h:h_krnl+(i*str_h),
                                                    j*str_w:w_krnl+(j*str_w)],
                                                    W[:, :, :, re]),
                                        axis=(1, 2, 3))
    return activation(H + b)
