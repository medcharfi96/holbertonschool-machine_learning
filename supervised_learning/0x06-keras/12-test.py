#!/usr/bin/env python3
""" task 12 """
import tensorflow.keras as K


def test_model(network, data, labels, verbose=True):
    """
    test de reseau neuronal
    :param network:
    :param data:
    :param labels:
    :param verbose:
    """
    zboub_safi = network.evaluate(data, labels, verbose=verbose)
    return zboub_safi
