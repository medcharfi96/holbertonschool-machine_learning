#!/usr/bin/env python3
""" task 0"""
import numpy as np


def convolve_grayscale_valid(images, kernel):
    """
    fonction de convultion
    :param images:
    :param kernel:
    """
    m = images.shape[0]
    tof_h = images.shape[1]
    tof_w = images.shape[2]
    krnl_h, krnl_w = kernel.shape
    res_h = tof_h - krnl_h + 1
    res_w = tof_w - krnl_w + 1
    retour = np.zeros((m, res_h, res_w))

    for x in range(res_h):
        for y in range(res_w):
            retour[:,  x, y] = (images[:, x:krnl_h+x, y:krnl_w+y] *
                                kernel).sum(axis=(1, 2))
    return retour
