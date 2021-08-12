#!/usr/bin/env python3
""" task 1 """
import tensorflow as tf


def crop_image(image, size):
    """
    recadrer limage
    :param image:
    :param size:
    :return:
    """

    img = tf.random_crop(image, size)
    return img
