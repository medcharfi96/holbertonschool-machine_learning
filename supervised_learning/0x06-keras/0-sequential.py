#!/usr/bin/env python3
""" task 0"""
import tensorflow.keras as K


def build_model(nx, layers, activations, lambtha, keep_prob):
    """
    classe neuronal
    :param nx: int
    :param layers: list
    :param activations: list
    :param lambtha: int
    :param keep_prob: prob int
    """
    model = K.Sequential()
    krnl = K.regularizers.l2(lambtha)
    model.add(K.layers.Dense(layers[0], activation=activations[0],
                             input_dim=nx, kernel_regularizer=krnl,
                             name='dense'))
    for i in range(1, len(layers)):
        model.add(K.layers.Dropout(1 - keep_prob))
        model.add(K.layers.Dense(layers[i], activation=activations[i],
                                 kernel_regularizer=krnl,
                                 name='dense'+str(i)))

    return model
