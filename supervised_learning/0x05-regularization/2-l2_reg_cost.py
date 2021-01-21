#!/usr/bin/env python3
""" task 2"""
import tensorflow as tf


def l2_reg_cost(cost):
    """
    fn de cost avec reg l2
    :param cost:
    """
    cost += tf.losses.get_regularization_losses()
    return cost
