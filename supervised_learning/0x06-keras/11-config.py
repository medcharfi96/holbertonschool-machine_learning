#!/usr/bin/env python3
""" task 11 """
import tensorflow.keras as K


def save_config(network, filename):
    """
    engestrer un model forme json
    :param network:
    :param filename:
    """
    with open(filename, "w") as fichier:
        fichier.write(network.to_json())
    return None


def load_config(filename):
    """
    telecharger un model
    :param filename:
    """
    with open(filename, "r") as fichier:
        mod_get = K.models.model_from_json(fichier.read())
    return mod_get
