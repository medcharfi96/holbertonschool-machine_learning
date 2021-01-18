#!/usr/bin/env python3
""" task 4 """
import numpy as np


def specificity(confusion):
    """
    des
    :param confusion:
    """
    diag = np.diag(confusion)
    faux_pos = np.sum(confusion, axis=0)
    faux_negatif = np.sum(confusion, axis=1)
    res = np.sum(confusion) - (faux_pos + faux_negatif - diag)
    return (res / (faux_pos - diag + res))
