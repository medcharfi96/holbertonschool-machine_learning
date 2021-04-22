#!/usr/bin/env python3
""" task 0 """


import tensorflow.keras as keras


def autoencoder(input_dims, hidden_layers, latent_dims):
    """
    encoder decodeer
    :param input_dims:
    :param hidden_layers:
    :param latent_dims:
    """
    # Encoder
    inpt_enco = keras.Input(shape=(input_dims,))

    enco = keras.layers.Dense(hidden_layers[0],
                              activation='relu')(inpt_enco)

    for i in range(1, len(hidden_layers)):
        enco = keras.layers.Dense(hidden_layers[i],
                                  activation='relu')(enco)

    output = keras.layers.Dense(latent_dims, activation='relu')(enco)
    encoder = keras.models.Model(inputs=inpt_enco, outputs=output)
    # Decoder
    inpt_dec = keras.Input(shape=(latent_dims,))
    deco = keras.layers.Dense(hidden_layers[-1],
                              activation='relu')(inpt_dec)

    for i in range(len(hidden_layers) - 2, -1, -1):
        deco = keras.layers.Dense(hidden_layers[i],
                                  activation='relu')(deco)

    output2 = keras.layers.Dense(input_dims, activation='sigmoid')(deco)

    decoder = keras.models.Model(inputs=inpt_dec, outputs=output2)

    out_encoder = encoder(inpt_enco)
    out_decoder = decoder(out_encoder)

    # Autoencoder
    autoencodeer = keras.models.Model(inputs=inpt_enco, outputs=out_decoder)
    autoencodeer.compile(optimizer='Adam', loss='binary_crossentropy')

    return encoder, decoder, autoencodeer
