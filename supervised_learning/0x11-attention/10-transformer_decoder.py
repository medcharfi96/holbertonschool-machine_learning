#!/usr/bin/env python3
""" task 9 """
import tensorflow as tf
positional_encoding = __import__('4-positional_encoding').positional_encoding
DecoderBlock = __import__('8-transformer_decoder_block').DecoderBlock


class Decoder(tf.keras.layers.Layer):
    """ classe decoder  """

    def __init__(self, N, dm, h, hidden,
                 target_vocab, max_seq_len, drop_rate=0.1):
        """
        constucteur
        :param N:
        :param dm:
        :param h:
        :param hidden:
        :param target_vocab:
        :param max_seq_len:
        :param drop_rate:
        """

        super(Decoder, self).__init__()

        self.N = N
        self.dm = dm
        self.embedding = tf.keras.layers.Embedding(target_vocab, dm)
        self.positional_encoding = positional_encoding(max_seq_len, dm)
        self.blocks = [DecoderBlock(dm, h, hidden, drop_rate)
                       for _ in range(N)]
        self.dropout = tf.keras.layers.Dropout(drop_rate)

    def call(self, x, encoder_output, training, look_ahead_mask, padding_mask):
        """
        desc
        :param x:
        :param encoder_output:
        :param training:
        :param look_ahead_mask:
        :param padding_mask:
        :return:
        """

        len_sequence = x.shape[1]

        x = self.embedding(x)
        x = x * tf.math.sqrt(tf.cast(self.dm, tf.float32))
        x = x + self.positional_encoding[:len_sequence]

        x = self.dropout(x, training=training)
        for j in range(self.N):
            x = self.blocks[j](x, encoder_output, training,
                               look_ahead_mask, padding_mask)
        return x
