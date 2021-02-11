#!/usr/bin/env python3
""" task 5"""
import tensorflow.keras as K


def dense_block(X, nb_filters, growth_rate, layers):
    """
    description
    :param X:
    :param nb_filters:
    :param growth_rate:
    :param layers:
    """
    krnl = K.initializers.he_normal()
    for count in range(layers):
        BN_prec = K.layers.BatchNormalization(axis=3)(X)
        ACT_prec = K.layers.Activation('relu')(BN_prec)
        CONV_1 = K.layers.Conv2D(filters=growth_rate*4,
                                 kernel_size=1,
                                 padding='same',
                                 kernel_initializer=krnl)(ACT_prec)
        BN_suiv = K.layers.BatchNormalization(axis=3)(CONV_1)
        ACT_suiv = K.layers.Activation('relu')(BN_suiv)
        CONV_3 = K.layers.Conv2D(filters=growth_rate,
                                 kernel_size=3,
                                 padding='same',
                                 kernel_initializer=krnl)(ACT_suiv)
        X = K.layers.concatenate([X, CONV_3])
        nb_filters = nb_filters + growth_rate

    return X, nb_filters
