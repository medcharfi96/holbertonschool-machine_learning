#!/usr/bin/env python3
""" task 3 """
import tensorflow.keras as K


def projection_block(A_prev, filters, s=2):
    """
    creation de bloc de projection
    :param A_prev:
    :param filters:
    :param s:
    """
    F11 = filters[0]
    F3 = filters[1]
    F12 = filters[2]
    krnl = K.initializers.he_normal()
    C1 = K.layers.Conv2D(filters=F11,
                         kernel_size=(1, 1),
                         padding='same',
                         strides=s,
                         kernel_initializer=krnl)(A_prev)
    NM1 = K.layers.BatchNormalization(axis=3)(C1)
    AV_C1 = K.layers.Activation('relu')(NM1)
    C2 = K.layers.Conv2D(filters=F3,
                         kernel_size=(3, 3),
                         padding='same',
                         kernel_initializer=krnl)(AV_C1)
    NM2 = K.layers.BatchNormalization(axis=3)(C2)
    AV_C2 = K.layers.Activation('relu')(NM2)
    C3 = K.layers.Conv2D(filters=F12,
                         kernel_size=(1, 1),
                         padding='same',
                         kernel_initializer=krnl)(AV_C2)
    NM3 = K.layers.BatchNormalization(axis=3)(C3)
    C4 = K.layers.Conv2D(filters=F12,
                         kernel_size=(1, 1),
                         padding='same',
                         strides=s,
                         kernel_initializer=krnl)(A_prev)
    NM4 = K.layers.BatchNormalization(axis=3)(C4)
    final = K.layers.Activation('relu')(K.layers.Add()([NM3, NM4]))
    return final
