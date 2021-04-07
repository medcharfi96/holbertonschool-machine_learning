#!/usr/bin/env python3
""" task 3 """


import numpy as np


def forward(Observation, Emission, Transition, Initial):
    """
    algorthme de chaine caché
    :param Observation:
    :param Emission:
    :param Transition:
    :param Initial:
    """

    if type(Observation) != np.ndarray:
        return None, None

    T = Observation.shape[0]
    if type(Emission) != np.ndarray:
        return None, None

    N = Emission.shape[0]
    if type(Transition) != np.ndarray:
        return None, None

    if type(Initial) != np.ndarray:
        return None, None

    F = np.zeros((N, T))
    F[:, 0] = np.multiply(Initial.T, Emission[:, Observation[0]])

    for i in range(1, T):
        for j in range(N):
            tr = Transition[:, j]
            ALF = Emission[j, Observation[i]]
            F[j, i] = np.sum(F[:, i - 1] * tr * ALF)

    P = F[:, -1:].sum()
    return P, F
