#!/usr/bin/env python3
""" task 0 """
import tensorflow as tf


def flip_image(image):
    """
    retourner limage horizontal
    :param image:
    :return:
    """

    img = tf.image.flip_left_right(image)
    return img
