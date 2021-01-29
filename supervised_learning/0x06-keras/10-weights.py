#!/usr/bin/env python3
""" task 10 """
import tensorflow.keras as K


def save_weights(network, filename, save_format='h5'):
    """
    enregistrer un model
    :param network:
    :param filename:
    :param save_format:
    """
    network.save_weights(filename, overwrite=True)
    return None


def load_weights(network, filename):
    """
    telecharger un model
    :param network:
    :param filename:
    """
    network.load_weights(filename)
    return None
