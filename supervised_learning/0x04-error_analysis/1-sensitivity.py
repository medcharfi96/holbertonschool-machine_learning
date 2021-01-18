#!/usr/bin/env python3
""" task 1 """
import numpy as np


def sensitivity(confusion):
    """
    des
    :param confusion:
    """
    pred = np.diag(confusion)
    somme = np.sum(confusion, axis=1)
    return (pred / somme)
