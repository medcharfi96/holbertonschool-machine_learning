#!/usr/bin/env python3
""" task 4"""
import numpy as np


def convolve_channels(images, kernel, padding='same', stride=(1, 1)):
    """

    :param images:
    :param kernel:
    :param padding:
    :param stride:
    :return:
    """

    m, tof_h, tof_w, nthing = np.shape(images)

    krnl_h, krnl_w, nthing1 = np.shape(kernel)

    sh, sw = stride

    if padding == 'same':
        pnd_h = int(((tof_h - 1) * sh + krnl_h - tof_h) / 2) + 1
        pnd_w = int(((tof_w - 1) * sw + krnl_w - tof_w) / 2) + 1
    if padding == 'valid':
        pnd_h = 0
        pnd_w = 0
    else:
        pnd_h = padding[0]
        pnd_w = padding[1]

    hfinal = int(((tof_h - krnl_h + (2 * pnd_h)) / sh) + 1)
    wfinal = int(((tof_w - krnl_w + (2 * pnd_w)) / sw) + 1)
    IMG_ret = np.zeros((m, hfinal, wfinal))

    images = np.pad(images, [(0, 0), (pnd_h, pnd_h),
                             (pnd_w, pnd_w), (0, 0)], 'constant')

    for fi in range(hfinal):
        for zi in range(wfinal):
            IMG_ret[:, fi, zi] = np.sum(kernel * (images[:,
                                                  fi*sh:fi*sh + krnl_h,
                                                  zi*sw:zi*sw + krnl_w]),
                                        axis=(1, 2, 3))

    return IMG_ret
