#!/usr/bin/env python3
"""
task 0
"""
import tensorflow as tf


def create_placeholders(nx, classes):
    """
    fonction de création de class place holder
    :param nx: int nb col
    :param classes: nb class
    :return:
    """
    x = tf.placeholder(tf.float32, shape=(None, nx), name='x')
    y = tf.placeholder(tf.float32, shape=[None, classes], name='y')
    return x, y
