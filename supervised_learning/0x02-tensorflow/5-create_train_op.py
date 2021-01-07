#!/usr/bin/env python3
"""
task 5
"""
import tensorflow as tf


def create_train_op(loss, alpha):
    """
    creation deentrenement operationel
    :param loss: int
    :param alpha: int
    """
    optimizer = tf.train.GradientDescentOptimizer(learning_rate=alpha)
    opt2 = optimizer.minimize(loss)
    return opt2
