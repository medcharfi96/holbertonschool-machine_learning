#!/usr/bin/env python3
""" task 1 """
import numpy as np


def q_init(env):
    """
    q table init
    :param env:
    """
    actions_taille = env.action_space.n
    states_taille = env.observation_space.n
    table = np.zeros((states_taille, actions_taille))
    return table
