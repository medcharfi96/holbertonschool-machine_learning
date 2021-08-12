#!/usr/bin/env python3
"""task 5 """
import tensorflow as tf


def change_hue(image, delta):
    """
    ajustement de coul
    :param image:
    :param delta:
    :return:
    """
    x = tf.image.adjust_hue(image, delta)
    return x
