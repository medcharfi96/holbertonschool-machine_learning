#!/usr/bin/env python3
""" task 9 """
import tensorflow.keras as K


def save_model(network, filename):
    """
    enregistrement de model
    :param network:
    :param filename:
    """
    network.save(filename)
    return None


def load_model(filename):
    """
    telechargement de model
    :param filename:
    """
    nt = K.models.load_model(filename)
    return nt
