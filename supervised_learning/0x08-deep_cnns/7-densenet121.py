#!/usr/bin/env python3
""" task 7"""
import tensorflow.keras as K
dense_block = __import__('5-dense_block').dense_block
transition_layer = __import__('6-transition_layer').transition_layer


def densenet121(growth_rate=32, compression=1.0):
    """
    desœ
    :param growth_rate:
    :param compression:
    """
    krnl = K.initializers.he_normal()
    XX = K.Input(shape=(224, 224, 3))
    BN_C0 = K.layers.BatchNormalization(axis=3)(XX)
    ACT_C0 = K.layers.Activation('relu')(BN_C0)

    C1 = K.layers.Conv2D(filters=growth_rate * 2,
                         strides=(2, 2),
                         padding='same',
                         kernel_size=(7, 7),
                         kernel_initializer=krnl)(ACT_C0)
    PL_C1 = K.layers.MaxPool2D(pool_size=(3, 3),
                               strides=(2, 2),
                               padding='same')(C1)

    C2, NB_fil = dense_block(PL_C1, 2*growth_rate, growth_rate, 6)
    C3, NB_fil3 = transition_layer(C2, NB_fil, compression)
    C4, NB_fil4 = dense_block(C3, NB_fil3, growth_rate, 12)
    C5, NB_fil5 = transition_layer(C4, NB_fil4, compression)
    C6, NB_fil6 = dense_block(C5, NB_fil5, growth_rate, 24)
    C7, NB_fil7 = transition_layer(C6, NB_fil6, compression)
    C8, n_f8 = dense_block(C7, NB_fil7, growth_rate, 16)

    moyenne = K.layers.AveragePooling2D(pool_size=(7, 7),
                                        strides=(1, 1),
                                        padding='same')(C8)
    YY = K.layers.Dense(1000, activation='softmax',
                        kernel_initializer=krnl)(moyenne)
    final = K.models.Model(inputs=XX,
                           outputs=YY)
    return final
