#!/usr/bin/env python3
""" task 3 """


import numpy as np


def viterbi(Observation, Emission, Transition, Initial):
    """
    calcule etat le plus chanceux
    :param Observation:
    :param Emission:
    :param Transition:
    :param Initial:
    """

    N = Emission.shape[0]
    T = Observation.shape[0]
    F = np.empty((N, T))
    prev = np.empty((N, T))

    F[:, 0] = Initial.T * Emission[:, Observation[0]]
    prev[:, 0] = 0

    for i in range(1, Observation.shape[0]):
        obs = Observation[i]
        F[:, i] = np.max(F[:, i] *
                         Transition.T *
                         Emission[np.newaxis, :, obs].T, 1)

        prev[:, i] = np.argmax(F[:, i - 1] * Transition.T, 1)

    path = T * [1]
    path[-1] = np.argmax(F[:, T - 1])
    idx = 1
    for i in range(T - 2, -1, -1):
        path[idx] = int(prev[int(path[0]), i])
        path[0] = prev[int(path[0]), i]
        idx += 1

    P = np.amax(F, axis=0)
    P = np.amin(P)

    return path, P
