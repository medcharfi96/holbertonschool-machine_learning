#!/usr/bin/env python3
""" task 0 """


import tensorflow as tf


class RNNEncoder(tf.keras.layers.Layer):
    """
    RNN encoder
    """

    def __init__(self, vocab, embedding, units, batch):
        """
        constructeur
        :param vocab:
        :param embedding:
        :param units:
        :param batch:
        """

        super(RNNEncoder, self).__init__()
        self.batch = batch
        self.units = units
        self.embedding = tf.keras.layers.Embedding(
            input_dim=vocab, output_dim=embedding)
        self.gru = tf.keras.layers.GRU(
            units,
            recurrent_initializer="glorot_uniform",
            return_sequences=True,
            return_state=True)

    def initialize_hidden_state(self):
        """
        inisialisation
        :return:
        """
        initializer = tf.keras.initializers.Zeros()
        hiden = initializer(shape=(self.batch, self.units))

        return hiden

    def call(self, x, initial):
        """
        desc
        :param x:
        :param initial:
        :return:
        """
        res = self.embedding(x)
        outs, hidden = self.gru(res, initial_state=initial)

        return outs, hidden
