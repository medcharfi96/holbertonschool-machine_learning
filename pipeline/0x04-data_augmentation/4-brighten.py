#!/usr/bin/env python3
"""task 4 """
import tensorflow as tf


def change_brightness(image, max_delta):
    """
    changer la brillance
    :param image:
    :param max_delta:
    :return:
    """
    brillance = tf.image.adjust_brightness(image, max_delta)
    return brillance
