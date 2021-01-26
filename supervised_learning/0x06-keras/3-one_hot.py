#!/usr/bin/env python3
"""task  3 """
import tensorflow.keras as k


def one_hot(labels, classes=None):
    """
    des
    :param labels:
    :param classes:
    """
    O_h = k.utils.to_categorical(labels, classes)
    return O_h
