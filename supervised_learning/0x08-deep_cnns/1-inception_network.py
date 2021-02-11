#!/usr/bin/env python3
""" task 1 """
import tensorflow.keras as K
inception_block = __import__('0-inception_block').inception_block


def inception_network():
    """
    construit le réseau de création
    """
    YY = K.Input(shape=(224, 224, 3))
    krnl = K.initializers.he_normal(seed=None)
    C1 = K.layers.Conv2D(filters=64,
                         kernel_size=(7, 7),
                         strides=(2, 2),
                         padding='same',
                         activation='relu',
                         use_bias=True,
                         kernel_initializer=krnl)(YY)
    PL_C1 = K.layers.MaxPooling2D(pool_size=(3, 3),
                                  strides=(2, 2),
                                  padding='same')(C1)
    C2 = K.layers.Conv2D(filters=64,
                         kernel_size=(1, 1),
                         activation='relu',
                         kernel_initializer=krnl)(PL_C1)
    C3 = K.layers.Conv2D(filters=192,
                         kernel_size=(3, 3),
                         padding='same',
                         activation='relu',
                         kernel_initializer=krnl)(C2)
    PL_C2 = K.layers.MaxPooling2D(pool_size=(3, 3),
                                  strides=(2, 2),
                                  padding='same')(C3)
    C31 = inception_block(PL_C2, [64, 96, 128, 16, 32, 32])
    C32 = inception_block(C31, [128, 128, 192, 32, 96, 64])
    PL_C3 = K.layers.MaxPooling2D(pool_size=(3, 3),
                                  strides=(2, 2),
                                  padding='same')(C32)
    INC_3 = inception_block(PL_C3, [192, 96, 208, 16, 48, 64])
    C4 = inception_block(INC_3, [160, 112, 224, 24, 64, 64])
    C5 = inception_block(C4, [128, 128, 256, 24, 64, 64])
    C6 = inception_block(C5, [112, 144, 288, 32, 64, 64])
    C7 = inception_block(C6, [256, 160, 320, 32, 128, 128])
    PL_C4 = K.layers.MaxPooling2D(pool_size=(3, 3),
                                  strides=(2, 2),
                                  padding='same')(C7)
    C8 = inception_block(PL_C4, [256, 160, 320, 32, 128, 128])
    C9 = inception_block(C8, [384, 192, 384, 48, 128, 128])
    moyenne = K.layers.AveragePooling2D(pool_size=(7, 7),
                                        strides=(1, 1))(C9)
    fn = K.layers.Dropout(0.4)(moyenne)
    XX = K.layers.Dense(units=1000,
                        activation='softmax',
                        kernel_initializer=krnl)(fn)
    resultat = K.models.Model(inputs=YY,
                              outputs=XX)
    return resultat
