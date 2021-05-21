#!/usr/bin/env python3
""" task 1"""


import tensorflow as tf


class SelfAttention(tf.keras.layers.Layer):
    """
    calcule attention
    """
    def __init__(self, units):
        """
        constructeur
        :param units:
        """
        super(SelfAttention, self).__init__()
        self.W = tf.keras.layers.Dense(units)
        self.U = tf.keras.layers.Dense(units)
        self.V = tf.keras.layers.Dense(1)

    def call(self, s_prev, hidden_states):
        """
        desc
        :param s_prev:
        :param hidden_states:
        :return:
        """

        Querry = tf.expand_dims(s_prev, axis=1)
        re1 = self.W(Querry)
        re2 = self.U(hidden_states)
        score = self.V(tf.nn.tanh(re1 + re2))
        poid = tf.nn.softmax(score, axis=1)
        cont = tf.reduce_sum((poid * hidden_states), axis=1)
        return cont, poid
