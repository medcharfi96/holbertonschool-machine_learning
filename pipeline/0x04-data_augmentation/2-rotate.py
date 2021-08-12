#!/usr/bin/env python3
"""task 2 """
import tensorflow as tf


def rotate_image(image):
    """
    rotation de limage
    :param image:
    :return:
    """

    img = tf.image.rot90(image, k=1)

    return img
