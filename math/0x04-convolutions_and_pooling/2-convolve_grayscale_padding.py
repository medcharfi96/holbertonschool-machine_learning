#!/usr/bin/env python3
""" convolve function """
import numpy as np


def convolve_grayscale_padding(images, kernel, padding):
    """
    ahhhhhhhhhhhhhhhhhhhhhhh
    :param images:
    :param kernel:
    :param padding:
    """
    krnl_h, krnl_w = np.shape(kernel)
    m, heigt, wight = np.shape(images)
    pnd_h, pnd_w = padding
    res_h = heigt + (2 * pnd_h) - krnl_h + 1
    res_w = wight + (2 * pnd_w) - krnl_w + 1

    IMG_retour = np.zeros((m, res_h, res_w))

    images = np.pad(images, [(0, 0), (pnd_h, pnd_h),
                             (pnd_w, pnd_w)], 'constant')
    for i in range(res_h):
        for j in range(res_w):
            IMG_retour[:, i, j] = (images[:, i: i + krnl_h, j: j + krnl_w]
                                   * kernel).sum(axis=(1, 2))
    return IMG_retour
