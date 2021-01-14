#!/usr/bin/env python3
"""
task1
"""


def normalize(X, m, s):
    """
    Function de normalisation
    """
    stand = (X - m) / s
    return stand
