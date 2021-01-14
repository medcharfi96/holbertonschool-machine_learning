#!/usr/bin/env python3
"""
task 10
"""
import tensorflow as tf


def create_Adam_op(loss, alpha, beta1, beta2, epsilon):
    """
    desc
    :param loss: int
    :param alpha: int
    :param beta1: int
    :param beta2: int
    :param epsilon: int
    """
    op = tf.train.AdamOptimizer(learning_rate=alpha, beta1=beta1,
                                beta2=beta2, epsilon=epsilon, name='Adam')
    tr = op.minimize(loss)
    return tr
