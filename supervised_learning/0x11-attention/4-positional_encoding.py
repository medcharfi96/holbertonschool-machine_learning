#!/usr/bin/env python3
"""task 3 """


import numpy as np


def positional_encoding(max_seq_len, dm):
    """
    calcilde encodage posisionel
    :param max_seq_len:
    :param dm:
    :return:
    """

    post_enco_v = np.zeros([max_seq_len, dm])

    for i in range(dm):
        for j in range(max_seq_len):
            post_enco_v[j, i] = j / np.power(10000, (2 * (i // 2) / dm))

    post_enco_v[:, 0::2] = np.sin(post_enco_v[:, 0::2])
    post_enco_v[:, 1::2] = np.cos(post_enco_v[:, 1::2])

    return post_enco_v
