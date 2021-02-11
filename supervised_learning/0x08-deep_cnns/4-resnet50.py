#!/usr/bin/env python3
""" task 4 """
import tensorflow._api.v1.keras as K
identity_block = __import__('2-identity_block').identity_block
projection_block = __import__('3-projection_block').projection_block


def resnet50():
    """
    creation de resnet50
    :return:
    """
    XX = K.Input(shape=(224, 224, 3))
    krnl = K.initializers.he_normal(seed=None)
    C1 = K.layers.Conv2D(filters=64,
                         kernel_size=(7, 7),
                         padding='same',
                         kernel_initializer=krnl)(XX)
    B1 = K.layers.BatchNormalization(axis=3)(C1)
    AC_C1 = K.layers.Activation('relu')(B1)
    PL_C1 = K.layers.MaxPooling2D(pool_size=(3, 3),
                                  strides=(2, 2),
                                  padding="same")(AC_C1)
    PR_1 = projection_block(PL_C1, [64, 64, 256], 1)
    L1 = identity_block(PR_1, [64, 64, 256])
    L2 = identity_block(L1, [64, 64, 256])
    PR_2 = projection_block(L2, [128, 128, 512])
    L3 = identity_block(PR_2, [128, 128, 512])
    L4 = identity_block(L3, [128, 128, 512])
    L5 = identity_block(L4, [128, 128, 512])
    PR_3 = projection_block(L5, [256, 256, 1024])
    L6 = identity_block(PR_3, [256, 256, 1024])
    L7 = identity_block(L6, [256, 256, 1024])
    L8 = identity_block(L7, [256, 256, 1024])
    L9 = identity_block(L8, [256, 256, 1024])
    L10 = identity_block(L9, [256, 256, 1024])
    PR_4 = projection_block(L10, [512, 512, 2048])
    L11 = identity_block(PR_4, [512, 512, 2048])
    L12 = identity_block(L11, [512, 512, 2048])
    moyenne = K.layers.AveragePooling2D(pool_size=(7, 7),
                                        padding='same',
                                        strides=(1, 1))(L12)
    YY = K.layers.Dense(units=1000,
                        activation='softmax',
                        kernel_initializer=krnl)(moyenne)
    model = K.models.Model(inputs=XX, outputs=YY)
    return model
