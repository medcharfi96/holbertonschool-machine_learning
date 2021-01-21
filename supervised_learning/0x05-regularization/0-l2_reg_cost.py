#!/usr/bin/env python3
"""
task 0
"""
import numpy as np


def l2_reg_cost(cost, lambtha, weights, L, m):
    """
    calucle de regaliszation par l2
    :param cost: la fn cost
    :param lambtha: int
    :param weights: poid int
    :param L: est le nombre de couches dans le réseau neuronal
    :param m: est le nombre de points de données utilisés
    """
    weight = 0
    for i in range(1, L+1):
        weight = weight + np.linalg.norm(weights['W' + str(i)])
    L2 = cost + (lambtha * (1 / (2 * m))) * weight
    return L2
