#!/usr/bin/env python3
""" task 1 """


import tensorflow._api.v1.keras as keras


def sparse(input_dims, hidden_layers, latent_dims, lambtha):
    """
    sparsing
    :param input_dims:
    :param hidden_layers:
    :param latent_dims:
    :param lambtha:
    """
    # Encoder
    inp_enco = keras.Input(shape=(input_dims, ))

    enco = keras.layers.Dense(hidden_layers[0],
                              activation='relu', )(inp_enco)

    for i in range(1, len(hidden_layers)):
        enco = keras.layers.Dense(hidden_layers[i],
                                  activation='relu')(enco)

    regulization = keras.regularizers.l1(lambtha)
    output = keras.layers.Dense(latent_dims,
                                activation='relu',
                                activity_regularizer=regulization)(enco)

    encoder = keras.Model(inputs=inp_enco, outputs=output)

    # Decoder
    inp_deco = keras.Input(shape=(latent_dims, ))
    deco = keras.layers.Dense(hidden_layers[-1],
                              activation='relu')(inp_deco)

    for i in range(len(hidden_layers)-2, -1, -1):
        deco = keras.layers.Dense(hidden_layers[i],
                                  activation='relu')(deco)
    output2 = keras.layers.Dense(input_dims,
                                 activation='sigmoid',)(deco)

    decoder = keras.Model(inputs=inp_deco, outputs=output2)

    output_encoder = encoder(inp_enco)
    output_decoder = decoder(output_encoder)

    autoencodeer = keras.models.Model(inputs=inp_enco, outputs=output_decoder)
    autoencodeer.compile(optimizer='Adam', loss='binary_crossentropy')

    return encoder, decoder, autoencodeer
