#!/usr/bin/env python3
"""
task 8
"""
import tensorflow as tf


def create_RMSProp_op(loss, alpha, beta2, epsilon):
    """
    DESCR
    """
    optimizer = tf.train.RMSPropOptimizer(alpha, decay=beta2, epsilon=epsilon,
                                          centered=False)
    return optimizer.minimize(loss)
