#!/usr/bin/env python3
""" task 1 """
import tensorflow as tf


def calculate_accuracy(y, y_pred):
    """
    calcule de precision
    :param y: int
    :param y_pred: sayeb zebi
    """
    hmed = tf.equal(tf.argmax(y, axis=1, name=None),
                    tf.argmax(y_pred, 1, name=None))
    ras_zebi_fil_brouklou = tf.reduce_mean(tf.cast(hmed, "float32", name=None))
    return ras_zebi_fil_brouklou
