#!/usr/bin/env python3
""" task 3"""
import tensorflow as tf


def l2_reg_create_layer(prev, n, activation, lambtha):
    """
    creation de layer  inclus l2
    :param prev: ancien
    :param n:  int
    :param activation: fn dactivation
    :param lambtha: int de reg
    """
    krnl = tf.contrib.layers.variance_scaling_initializer(mode="FAN_AVG")
    reg = tf.contrib.layers.l2_regularizer(lambtha)
    LY = tf.layers.Dense(units=n, activation=activation,
                         use_bias=True,
                         kernel_initializer=krnl,
                         kernel_regularizer=reg,
                         bias_regularizer=None)
    return LY(prev)
