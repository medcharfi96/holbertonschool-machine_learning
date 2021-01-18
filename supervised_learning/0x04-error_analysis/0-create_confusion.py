#!/usr/bin/env python3
""" task 0 """
import numpy as np


def create_confusion_matrix(labels, logits):
    """
    function de confusion
    :param labels: ligne
    :param logits: liste de predaction
    :return:
    """
    res = np.zeros((labels.shape[1], labels.shape[1]))
    res = np.dot(labels.T, logits)
    return res
