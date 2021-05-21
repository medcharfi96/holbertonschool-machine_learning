#!/usr/bin/env python3
"""task 4 """


import tensorflow as tf


def sdp_attention(Q, K, V, mask=None):
    """
    calcule de escale de point
    :param Q:
    :param K:
    :param V:
    :param mask:
    :return:
    """

    qk_pt = tf.matmul(Q, K, transpose_b=True)
    dk = tf.cast(tf.shape(K)[-1], tf.float32)

    scaled_lg = qk_pt / tf.math.sqrt(dk)

    if mask is not None:
        qk_pt += (mask * -1e9)

    poid = tf.nn.softmax(scaled_lg, axis=-1)
    out = tf.matmul(poid, V)

    return out, poid
