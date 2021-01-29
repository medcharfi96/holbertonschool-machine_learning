#!/usr/bin/env python3
""" task 13 """
import tensorflow.keras as K


def predict(network, data, verbose=False):
    """
    fonction de prediction
    :param network:
    :param data:
    :param verbose:
    """
    lahachwa_jet_fnouna = network.predict(data, verbose=verbose)
    return lahachwa_jet_fnouna
