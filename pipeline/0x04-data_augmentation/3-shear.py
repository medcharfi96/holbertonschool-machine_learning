#!/usr/bin/env python3
"""task 3 """
import tensorflow as tf


def shear_image(image, intensity):
    """
    kosha
    :param image:
    :param intensity:
    :return:
    """

    ret = tf.keras.preprocessing.image.img_to_array(image)
    sheea = tf.keras.preprocessing.image.random_shear(ret,
                                                      intensity,
                                                      row_axis=0,
                                                      col_axis=1,
                                                      channel_axis=2)
    img_ret = tf.keras.preprocessing.image.array_to_img(sheea)

    return img_ret
