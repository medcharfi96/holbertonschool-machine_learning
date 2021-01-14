#!/usr/bin/env python3
"""
Normalize
"""


def normalize(X, m, s):
    """
    Function de normalisation
    """
    stand = (X - m) / s
    return stand
