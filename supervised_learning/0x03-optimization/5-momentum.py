#!/usr/bin/env python3
"""
task 5
"""
import numpy as np


def update_variables_momentum(alpha, beta1, var, grad, v):
    """
    Function de calcule de moment
    """
    v1 = (beta1 * v) + np.multiply((1 - beta1), grad)
    var1 = var - (alpha * v1)
    return var1, v1
