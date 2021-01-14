#!/usr/bin/env python3
"""
task 12
"""
import tensorflow as tf


def learning_rate_decay(alpha, decay_rate, global_step, decay_step):
    """
    desc
    :param alpha: int
    :param decay_rate: int
    :param global_step: int
    :param decay_step: int
    """
    tbr = tf.train.inverse_time_decay(alpha, global_step, decay_step,
                                      decay_rate=decay_rate, staircase=True)
    return tbr
