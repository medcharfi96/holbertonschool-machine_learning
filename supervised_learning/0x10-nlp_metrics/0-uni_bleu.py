#!/usr/bin/env python3
""" task 0 """


import numpy as np


def uni_bleu(references, sentence):
    """
    calcule de unigram  Bleu
    :param references:list
    :param sentence: list
    """

    out_len = len(sentence)
    referance_l = []
    flat = {}

    # References and sentences
    for r in references:
        referance_l.append(len(r))

        for w in r:
            if w in sentence:
                if not flat.keys() == w:
                    flat[w] = 1

    flat_sum = sum(flat.values())
    ##idx_proche = np.argmin([abs(len(x) - out_len) for x in references])
    idx_proche = np.argmin(np.abs(referance_l - out_len))
    closest_len_refer = len(references[idx_proche])

    if out_len > closest_len_refer:
        bp = 1
    else:
        bp = np.exp(1 - float(closest_len_refer) / float(out_len))

    return bp * (flat_sum / out_len)
