#!/usr/bin/env python3
""" task  """
import tensorflow as tf


def calculate_loss(y, y_pred):
    """
    calcule de perte
    :param y: espace res
    :param y_pred: le estim
    """
    zok_secretaire = tf.losses.softmax_cross_entropy(y, logits=y_pred,
                                                     weights=1.0, scope=None)
    return (zok_secretaire)
