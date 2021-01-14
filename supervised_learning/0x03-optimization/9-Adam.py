#!/usr/bin/env python3
"""
task 9
"""


def update_variables_Adam(alpha, beta1, beta2, epsilon, var, grad, v, s, t):
    """
    desc
    :param alpha: int
    :param beta1: int
    :param beta2: int
    :param epsilon: int
    :param var: int
    :param grad: int
    :param v: int
    :param s: int
    :param t: int
    """
    mm = ((1 - beta1) * grad) + (beta1 * v)
    rms = (1 - beta2) * pow(grad, 2) + s * beta2
    mm_cor = mm / (1 - pow(beta1, t))
    rmss_cor = rms / (1 - pow(beta2, t))
    ZAB = var - alpha * (mm_cor / ((rmss_cor ** 0.5) + epsilon))
    return ZAB, mm, rms
