#!/usr/bin/env python3
""" task 6"""
import tensorflow.keras as K
from scipy.special.cython_special import ker


def transition_layer(X, nb_filters, compression):
    """
    fonction de construction de de layer de transission
    :param X:
    :param nb_filters:
    :param compression:
    """
    krnl = K.initializers.he_normal()
    XX = int(compression * nb_filters)

    BN1 = K.layers.BatchNormalization()(X)
    ACT1 = K.layers.Activation('relu')(BN1)
    C = K.layers.Conv2D(filters=XX, kernel_size=(1, 1),
                        padding='same',
                        kernel_initializer=krnl)(ACT1)
    moyenne = K.layers.AveragePooling2D(pool_size=(2, 2),
                                        strides=(2, 2),
                                        padding='same')(C)
    return moyenne, XX
