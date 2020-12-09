#!/usr/bin/env python3
"""adv"""


def np_slice(matrix, axes={}):
    """des"""
    cd = matrix.shape
    va = []
    for a in range(0, len(cd)):
        va.append(slice(*axes.get(a, (None, None))))
    return matrix[tuple(va)]
