#!/usr/bin/env python3
""" task 7"""


def early_stopping(cost, opt_cost, threshold, patience, count):
    """
    condinital of stop
    :param cost:
    :param opt_cost:
    :param threshold:
    :param patience:
    :param count:
    """
    if (opt_cost - threshold) <= cost:
        count += 1
    else:
        count = 0
    if (count != patience):
        res = False
    else:
        res = True
    return (res, count)
