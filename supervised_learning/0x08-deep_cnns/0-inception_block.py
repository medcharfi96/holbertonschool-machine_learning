#!/usr/bin/env python3
""" task 0 """
import tensorflow.keras as K


def inception_block(A_prev, filters):
    """
    description de bloc
    :param A_prev:
    :param filters:
    """
    F1 = filters[0]
    F3R = filters[1]
    F3 = filters[2]
    F5R = filters[3]
    F5 = filters[4]
    FPP = filters[5]
    he_init = K.initializers.he_normal()
    CF1 = K.layers.Conv2D(filters=F1, kernel_size=(1, 1),
                          padding='same',
                          activation='relu',
                          kernel_initializer=he_init)(A_prev)
    CF3R = K.layers.Conv2D(filters=F3R,
                           kernel_size=(1, 1),
                           padding='same',
                           activation='relu',
                           kernel_initializer=he_init)(A_prev)
    CF3 = K.layers.Conv2D(filters=F3,
                          kernel_size=3,
                          padding='same',
                          activation='relu',
                          kernel_initializer=he_init)(CF3R)
    CF5R = K.layers.Conv2D(filters=F5R,
                           kernel_size=(1, 1),
                           padding='same',
                           activation='relu',
                           kernel_initializer=he_init)(A_prev)
    CF5 = K.layers.Conv2D(filters=F5,
                          kernel_size=(5, 5),
                          padding='same',
                          activation='relu',
                          kernel_initializer=he_init)(CF5R)
    M_pooling = K.layers.MaxPooling2D(pool_size=(3, 3),
                                      strides=1,
                                      padding='same')(A_prev)
    C_FPP = K.layers.Conv2D(filters=FPP,
                            kernel_size=1,
                            padding='same',
                            activation='relu',
                            kernel_initializer=he_init)(M_pooling)
    zab = [CF1, CF3, CF5, C_FPP]
    fnl = K.layers.concatenate(zab)
    return fnl
