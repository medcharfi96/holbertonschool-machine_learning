#!/usr/bin/env python3
""" task 1 """
import numpy as np


def precision(confusion):
    """
    des
    :param confusion:
    """
    pred = np.diag(confusion)
    somme = np.sum(confusion, axis=0)
    return (pred / somme)
