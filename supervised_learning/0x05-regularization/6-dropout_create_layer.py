#!/usr/bin/env python3
""" task 6"""
import tensorflow as tf


def dropout_create_layer(prev, n, activation, keep_prob):
    """
    creation de lay de neurone connection
    :param prev:
    :param n:
    :param activation:
    :param keep_prob:
    """
    krnl = tf.contrib.layers.variance_scaling_initializer(mode="FAN_AVG")
    reg = tf.layers.Dropout(keep_prob)
    aasba = tf.layers.Dense(units=n,
                            activation=activation,
                            kernel_initializer=krnl,
                            kernel_regularizer=reg,
                            bias_regularizer=None,
                            name='layer')
    return aasba(prev)
