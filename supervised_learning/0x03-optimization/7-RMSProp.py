#!/usr/bin/env python3
"""
task 7
"""
import numpy as np


def update_variables_RMSProp(alpha, beta2, epsilon, var, grad, s):
    """
    desc
    :param alpha:
    :param beta2:
    :param epsilon:
    :param var:
    :param grad:
    :param s:
    :return:
    """
    s = (1 - beta2) * pow(grad, 2) + s * beta2
    var = var - alpha * grad / (np.sqrt(s) + epsilon)
    return var, s
