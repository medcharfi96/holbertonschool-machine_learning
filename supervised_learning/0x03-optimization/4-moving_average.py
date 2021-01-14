#!/usr/bin/env python3
"""
task 4
"""


def moving_average(data, beta):
    """ descrip"""
    res = []
    moy = 0
    for i in range(len(data)):
        moy = (1 - beta) * data[i] + beta * moy
        bc = moy / (1 - beta ** (i+1))
        res.append(bc)
    return res
