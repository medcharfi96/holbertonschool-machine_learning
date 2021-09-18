#!/usr/bin/env python3
""" task 2 """
import numpy as np


def epsilon_greedy(Q, state, epsilon):
    """
    prochain index
    :param Q:
    :param state:
    :param epsilon:
    """
    if np.random.uniform(0, 1) < epsilon:
        z = np.random.randint(0, Q.shape[1])
