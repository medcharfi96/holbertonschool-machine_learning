#!/usr/bin/env python3
""" task 1"""
import numpy as np


def convolve_grayscale_same(images, kernel):
    """
    convultion de ressemblance
    :param images: limage a trété
    :param kernel: le matrix de traitement
    :return: rabbi ykadrna aala fe3l l5ir
    """

    m = images.shape[0]
    tof_h = images.shape[1]
    tof_w = images.shape[2]
    krnl_h, krnl_w = kernel.shape
    if krnl_h % 2:
        tas = int((krnl_h - 1) / 2)
    else:
        tas = int(krnl_h / 2)
    if krnl_w % 2:
        wra = int((krnl_w - 1) / 2)
    else:
        wra = int(krnl_w / 2)
    res_w = tof_w - krnl_w + 1 + (2 * wra)
    res_h = tof_h - krnl_h + 1 + (2 * tas)
    convoluted = np.zeros((m, res_h, res_h))
    images = np.pad(images, [(0, 0), (tas, tas), (wra, wra)], 'constant')
    for i in range(res_h):
        for j in range(res_w):
            convoluted[:, j, i] = np.multiply(
                images[:, i:krnl_h+i, j:krnl_w+j], kernel).sum(axis=(1, 2))
    return convoluted
