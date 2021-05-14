#!/usr/bin/env python3
""" task 1 """


import numpy as np


def ngram_bleu(references, sentence, n):
    """
    calcule de  n  gram
    :param references:list
    :param sentence:list
    :param n: int
    """

    referenc_l = []
    flat = {}

    sent = [' '.join([str(ze) for ze in sentence[id:id + n]])
            for id in range(len(sentence) - (n - 1))]
    N_out_sent = (len(sent))

    for refs in references:
        refera_N = [' '.join([str(ze) for ze in refs[id:id + n]])
                    for id in range(len(sentence) - (n - 1))]

        referenc_l.append(len(refs))

        for word in refera_N:
            if word in sent:
                if not flat.keys() == word:
                    flat[word] = 1

    flat_sum = sum(flat.values())
    idx_proche = np.argmin([abs(len(x) - N_out_sent) for x in references])
    idx_proche_l = len(references[idx_proche])

    if N_out_sent <= idx_proche_l:
        bp = np.exp(1 - (idx_proche_l / len(sentence)))
    else:
        bp = 1
    return bp * (flat_sum / N_out_sent)
