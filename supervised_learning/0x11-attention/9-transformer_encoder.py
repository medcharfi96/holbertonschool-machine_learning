#!/usr/bin/env python3
""" tas 9 """
import tensorflow as tf


positional_encoding = __import__('4-positional_encoding').positional_encoding
EncoderBlock = __import__('7-transformer_encoder_block').EncoderBlock


class Encoder(tf.keras.layers.Layer):
    """ class description"""

    def __init__(self, N, dm, h,
                 hidden, input_vocab, max_seq_len, drop_rate=0.1):
        """
        constructeur
        :param N:
        :param dm:
        :param h:
        :param hidden:
        :param input_vocab:
        :param max_seq_len:
        :param drop_rate:
        """

        super(Encoder, self).__init__()
        self.N = N
        self.dm = dm
        self.embedding = tf.keras.layers.Embedding(input_vocab, dm)
        self.positional_encoding = positional_encoding(max_seq_len, self.dm)
        self.blocks = [EncoderBlock(dm, h, hidden, drop_rate)
                       for n in range(self.N)]
        self.dropout = tf.keras.layers.Dropout(drop_rate)

    def call(self, x, training, mask):
        """
        description
        :param x:
        :param training:
        :param mask:
        """

        seq_len = x.shape[1]
        x = self.embedding(x)
        x = x * tf.math.sqrt(tf.cast(self.dm, tf.float32))
        x = x + self.positional_encoding[:seq_len]

        output = self.dropout(x, training=training)
        for j in range(self.N):
            output = self.blocks[j](output, training, mask)
        return output
