#!/usr/bin/env python3
""" task 1"""
import tensorflow.keras as K


def build_model(nx, layers, activations, lambtha, keep_prob):
    """

    :param nx:
    :param layers:
    :param activations:
    :param lambtha:
    :param keep_prob:
    """
    za = K.Input(shape=(nx,))
    reg = K.regularizers.l2(lambtha)
    va = K.layers.Dense(layers[0],
                        activation=activations[0],
                        kernel_regularizer=reg)(za)

    for count in range(1, len(layers)):
        va = K.layers.Dense(layers[count],
                            activation=activations[count],
                            kernel_regularizer=reg,
                            name='dense_'+str(count))(va)
        if count < len(layers) - 1:
            va = K.layers.Dropout(1-keep_prob)(va)
    model = K.Model(inputs=za, outputs=va)
    return model
