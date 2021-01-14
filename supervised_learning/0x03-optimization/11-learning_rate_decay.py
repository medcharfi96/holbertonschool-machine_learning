#!/usr/bin/env python3
"""
task 11
"""


import numpy as np


def learning_rate_decay(alpha, decay_rate, global_step, decay_step):
    """
    dessc
    """

    zeb = alpha / (1 + (decay_rate * np.floor(global_step / decay_step)))
    return zeb
