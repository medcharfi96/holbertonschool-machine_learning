#!/usr/bin/env python3
""" task3 """
import numpy as np


def convolve_grayscale(images, kernel, padding='same',
                       stride=(1, 1)):
    """
    :param images:
    :param kernel:
    :param padding:
    :param stride:
    :return:
    """
    m = images.shape[0]
    heigt = images.shape[1]
    wight = images.shape[2]
    krnl_h, krnl_w = np.shape(kernel)
    str_h, str_w = stride
    if padding == "valid":
        pnd_h = 0
        pnd_w = 0
    elif padding == "same":
        pnd_h = int(((heigt - 1) * str_h + krnl_h - heigt) / 2) + 1
        pnd_w = int(((wight - 1) * str_w + krnl_w - wight) / 2) + 1
    else:
        pnd_h = padding.shape[0]
        pnd_w = padding.shape[1]
    res_h = int(((heigt - krnl_h + (2 * pnd_h)) / str_h) + 1)
    res_w = int(((wight - krnl_w + (2 * pnd_w)) / str_w) + 1)
    image_ret = np.zeros((m, res_h, res_w))
    images = np.pad(images, [(0, 0), (pnd_h, pnd_h),
                             (pnd_w, pnd_w)], 'constant')
    for i in range(res_h):
        for j in range(res_w):
            image_ret[:, i, j] = np.sum(images[:,
                                        str_h * i:str_h * i + krnl_h,
                                        str_w * j:str_w * j + krnl_w] * kernel,
                                        axis=(1, 2))
    return image_ret
