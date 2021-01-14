#!/usr/bin/env python3
"""
task 13
"""
import numpy as np


def batch_norm(Z, gamma, beta, epsilon):
    """
    deesc
    """
    m = Z.shape[0]
    VA = np.sum(Z, axis=0) / m
    RE = (Z - VA) / (Z.var(0) + epsilon) ** 0.5
    ret = RE * gamma + beta
    return ret
