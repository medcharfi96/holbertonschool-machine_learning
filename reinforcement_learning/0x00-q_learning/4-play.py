#!/usr/bin/env python3
"""task 4 """
import numpy as np


def play(env, Q, max_steps=100):
    """
    agent entrainé
    :param env:
    :param Q:
    :param max_steps:
    """
    state = env.reset()
    done = False
    env.render()
    for _ in range(max_steps):
        action = np.argmax(Q[state, :])
        state, reward, done, info = env.step(action)
        env.render()
        if done is True:
            break
    return reward
