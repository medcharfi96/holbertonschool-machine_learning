#!/usr/bin/env python3
"""task 6 """


import tensorflow as tf
sdp_attention = __import__('5-sdp_attention').sdp_attention


class MultiHeadAttention(tf.keras.layers.Layer):
    """ descrption de classe"""

    def __init__(self, dm, h):
        """
        constrructeur
        :param dm:
        :param h:
        """

        super(MultiHeadAttention, self).__init__()
        self.h = h
        self.dm = dm
        self.depth = int(self.dm // self.h)
        self.Wq = tf.keras.layers.Dense(dm)
        self.Wk = tf.keras.layers.Dense(dm)
        self.Wv = tf.keras.layers.Dense(dm)
        self.linear = tf.keras.layers.Dense(dm)

    def splitHeads(self, rt, batch):
        """
        deviser le model
        :param m:
        :param batch:
        :return:
        """
        rt = tf.reshape(rt, (batch, -1, self.h, self.depth))
        return tf.transpose(rt, perm=[0, 2, 1, 3])

    def call(self, Q, K, V, mask):
        """
        desc
        :param Q:
        :param K:
        :param V:
        :param mask:
        :return:
        """

        B_size = tf.shape(K)[0]
        Q = self.Wq(Q)
        K = self.Wk(K)
        V = self.Wv(V)

        Q = self.splitHeads(Q, B_size)
        K = self.splitHeads(K, B_size)
        V = self.splitHeads(V, B_size)

        out, poid = sdp_attention(Q, K, V, mask)

        out = tf.transpose(out, perm=[0, 2, 1, 3])
        out = tf.reshape(out, (B_size, -1, self.dm))
        out = self.linear(out)

        return out, poid
