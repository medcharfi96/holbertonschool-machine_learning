#!/usr/bin/env python3
""" task 2 """
import tensorflow.keras as keras


def autoencoder(input_dims, filters, latent_dims):
    """
    convulution
    :param input_dims:
    :param filters:
    :param latent_dims:
    """
    # Encoder
    inp_enco = keras.Input(shape=input_dims)

    enco = keras.layers.Conv2D(filters=filters[0],
                               kernel_size=(3, 3), padding='same',
                               activation='relu')(inp_enco)
    enco = keras.layers.MaxPool2D(pool_size=(2, 2), padding='same')(enco)

    for i in range(1, len(filters)):
        enco = keras.layers.Conv2D(filters=filters[i],
                                   kernel_size=(3, 3),
                                   padding='same',
                                   activation='relu')(enco)
        enco = keras.layers.MaxPool2D(pool_size=(2, 2),
                                      padding='same')(enco)

    encoder = keras.models.Model(inputs=inp_enco, outputs=enco)

    # Decoder
    inpt_deco = keras.Input(shape=latent_dims)

    deco = keras.layers.Conv2D(filters=filters[-1],
                               kernel_size=(3, 3),
                               padding='same',
                               activation='relu')(inpt_deco)
    deco = keras.layers.UpSampling2D(2)(deco)

    for i in range(len(filters)-2, 0, -1):
        deco = keras.layers.Conv2D(filters=filters[i],
                                   kernel_size=3,
                                   padding='same',
                                   activation='relu')(deco)
        deco = keras.layers.UpSampling2D(2)(deco)

    deco = keras.layers.Conv2D(filters=filters[0],
                               kernel_size=(3, 3),
                               padding='valid',
                               activation='relu')(deco)
    deco = keras.layers.UpSampling2D(2)(deco)

    output = keras.layers.Conv2D(filters=input_dims[-1],
                                 kernel_size=3,
                                 padding='same',
                                 activation='sigmoid')(deco)

    decoder = keras.Model(inputs=inpt_deco, outputs=output)

    output_encoder = encoder(inp_enco)
    output_decoder = decoder(output_encoder)

    # Autoencoder
    autoencodeer = keras.models.Model(inputs=inp_enco, outputs=output_decoder)
    autoencoder().compile(optimizer='Adam',
                          loss='binary_crossentropy')

    return encoder, decoder, autoencodeer
