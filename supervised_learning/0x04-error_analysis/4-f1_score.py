#!/usr/bin/env python3
""" task 5"""
sensitivity = __import__('1-sensitivity').sensitivity
precision = __import__('2-precision').precision


def f1_score(confusion):
    """
    clacule de F1
    :param confusion: formule 2 * rap * prs /(rap + pres)
    """
    s = sensitivity(confusion)
    p = precision(confusion)
    f = 2 * ((p*s) / (p+s))
    return f
