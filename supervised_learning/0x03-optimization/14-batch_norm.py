#!/usr/bin/env python3
"""
task 14
"""


import tensorflow as tf


def create_batch_norm_layer(prev, n, activation):
    """
    desc
    """
    krnl = tf.contrib.layers.variance_scaling_initializer(mode="FAN_AVG")
    layer = tf.layers.Dense(units=n, kernel_initializer=krnl,
                            name="layer")
    x = layer(prev)
    mean, var = tf.nn.moments(x, [0])
    beta = tf.Variable(tf.zeros([n]))
    gama = tf.Variable(tf.ones([x.get_shape()[-1]]))
    res = tf.nn.batch_normalization(x, mean, var, offset=beta,
                                    scale=gama, variance_epsilon=1e-8)
    return activation(res)
