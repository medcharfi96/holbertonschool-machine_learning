#!/usr/bin/env python3
"""task 2 """
import tensorflow.keras as K


def optimize_model(network, alpha, beta1, beta2):
    """
    :param network:
    :param alpha:
    :param beta1:
    :param beta2:
    """
    optima = K.optimizers.Adam(lr=alpha, beta_1=beta1, beta_2=beta2)
    network.compile(optima, 'categorical_crossentropy', metrics=['accuracy'])
    return None
