#!/usr/bin/env python3
""" task 2 """
import tensorflow.keras as K


def identity_block(A_prev, filters):
    """
    construction de bloc
    :param A_prev:
    :param filters:
    """
    F11 = filters[0]
    F3 = filters[1]
    F12 = filters[2]
    krnl = K.initializers.he_normal(seed=None)

    C1 = K.layers.Conv2D(filters=F11, kernel_size=2,
                         padding='same',
                         kernel_initializer=krnl)(A_prev)

    NM1 = K.layers.BatchNormalization(axis=3)(C1)
    AV_C1 = K.layers.Activation('relu')(NM1)

    C2 = K.layers.Conv2D(filters=F3,
                         kernel_size=2,
                         padding='same',
                         kernel_initializer=krnl)(AV_C1)

    NM2 = K.layers.BatchNormalization(axis=3)(C2)
    AV_C2 = K.layers.Activation('relu')(NM2)

    C3 = K.layers.Conv2D(filters=F12,
                         kernel_size=2,
                         padding='same',
                         kernel_initializer=krnl)(AV_C2)

    NM3 = K.layers.BatchNormalization(axis=3, beta_initializer='zeros')(C3)
    X = K.layers.Add()([NM3, A_prev])
    final = K.layers.Activation('relu')(X)
    return final
