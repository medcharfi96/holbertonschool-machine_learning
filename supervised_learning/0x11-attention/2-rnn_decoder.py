#!/usr/bin/env python3
"""task 2 """


import tensorflow as tf
SelfAttention = __import__('1-self_attention').SelfAttention


class RNNDecoder(tf.keras.layers.Layer):
    """
    callse decoder
    """

    def __init__(self, vocab, embedding, units, batch):
        """
        constructeur
        :param vocab:
        :param embedding:
        :param units:
        :param batch:
        """

        super(RNNDecoder, self).__init__()
        self.embedding = tf.keras.layers.Embedding(
            input_dim=vocab, output_dim=embedding)
        self.gru = tf.keras.layers.GRU(
            units,
            recurrent_initializer="glorot_uniform",
            return_sequences=True,
            return_state=True)
        self.F = tf.keras.layers.Dense(vocab)

    def call(self, x, s_prev, hidden_states):
        """
        desc
        :param x:
        :param s_prev:
        :param hidden_states:
        :return:
        """
        attention = SelfAttention(s_prev.shape[1])
        cont, poid = attention(s_prev, hidden_states)
        x = self.embedding(x)
        res = tf.concat([tf.expand_dims(cont, 1), x], axis=-1)
        decode_O, state = self.gru(res)

        decode_O = tf.reshape(decode_O, (-1, decode_O.shape[2]))
        yev = self.F(decode_O)

        return yev, state
