#!/usr/bin/env python3
""" task 6"""
import tensorflow as tf


def create_momentum_op(loss, alpha, beta1):
    """
    optimisation de reaseau neuronal
    :param loss: int
    :param alpha: int
    :param beta1: int
    """
    operation = tf.train.MomentumOptimizer(alpha, beta1)
    return operation.minimize(loss)
