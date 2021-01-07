#!/usr/bin/env python3
""" task 1 """
import tensorflow as tf


def create_layer(prev, n, activation):
    """
    fonction de creation de layer
    """
    deb = tf.contrib.layers.variance_scaling_initializer(mode="FAN_AVG")
    layer = tf.layers.Dense(units=n, activation=activation,
                            kernel_initializer=deb, kernel_constraint=None,
                            name='layer')

    return layer(prev)
