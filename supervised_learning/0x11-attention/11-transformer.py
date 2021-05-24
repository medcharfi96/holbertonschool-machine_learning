#!/usr/bin/env python3
""" task 10 """


import tensorflow as tf
Encoder = __import__('9-transformer_encoder').Encoder
Decoder = __import__('10-transformer_decoder').Decoder


class Transformer(tf.keras.Model):
    """ classe transformer"""

    def __init__(self, N, dm, h, hidden, input_vocab, target_vocab,
                 max_seq_input, max_seq_target, drop_rate=0.1):
        """
        constructeur
        :param N:
        :param dm:
        :param h:
        :param hidden:
        :param input_vocab:
        :param target_vocab:
        :param max_seq_input:
        :param max_seq_target:
        :param drop_rate:
        """
        super().__init__()
        self.encoder = Encoder(N, dm, h, hidden, input_vocab,
                               max_seq_input, drop_rate)
        self.decoder = Decoder(N, dm, h, hidden, target_vocab,
                               max_seq_target, drop_rate)
        self.linear = tf.keras.layers.Dense(target_vocab)

    def call(self, inputs, target, training, encoder_mask,
             look_ahead_mask, decoder_mask):
        """
        description
        :param inputs:
        :param target:
        :param training:
        :param encoder_mask:
        :param look_ahead_mask:
        :param decoder_mask:
        """

        encood_out = self.encoder(inputs, training, encoder_mask)

        decod_out = self.decoder(target,
                                 encood_out,
                                 training,
                                 look_ahead_mask,
                                 decoder_mask)
        resultat = self.linear(decod_out)

        return resultat
