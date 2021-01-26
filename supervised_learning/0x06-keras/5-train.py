#!/usr/bin/env python3
""" task 4"""
import tensorflow.keras as K


def train_model(network, data, labels, batch_size, epochs,
                validation_data=None, verbose=True, shuffle=False):
    """
    des
    :param network:
    :param data:
    :param labels:
    :param batch_size:
    :param epochs:
    :param verbose:
    :param shuffle:
    """
    history = network.fit(x=data, y=labels,
                          epochs=epochs,
                          batch_size=batch_size,
                          verbose=verbose,
                          shuffle=shuffle,
                          validation_data=validation_data)
    return history
