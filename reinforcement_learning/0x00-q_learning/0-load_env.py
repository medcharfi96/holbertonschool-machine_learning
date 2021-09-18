#!/usr/bin/env python3
"""task 0 """
import gym


def load_frozen_lake(desc=None, map_name=None, is_slippery=False):
    """
    load frozen lake
    :param desc:
    :param map_name:
    :param is_slippery:
    """
    if desc is None and map_name is None:
        env = gym.make('FrozenLake8x8-v0')
    else:
        env = gym.make('FrozenLake-v0',
                       desc=desc,
                       map_name=map_name,
                       is_slippery=is_slippery)
    return env
