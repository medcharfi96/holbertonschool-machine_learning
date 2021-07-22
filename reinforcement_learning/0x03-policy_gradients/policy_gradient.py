#!/usr/bin/env python3
"""
policy  function
"""
import numpy as np


def softmax_grad(probs):
    """Vectorized softmax"""
    s = probs.reshape(-1, 1)
    return np.diagflat(s) - np.dot(s, s.T)


def softmax(vector):
    """softmax function"""
    e = np.exp(vector)
    return e / e.sum()


def policy(matrix, weight):
    """
    fn de policy
    :param matrix:
    :param weight:
    """
    z = matrix.dot(weight)
    exp = np.exp(z)

    return exp / np.sum(exp)


def policy_gradient(state, weight):
    """
    calculate the Monte acrlo policy
    :param state:
    :param weight:
    """
    probs = policy(state, weight)
    action = np.random.choice(2, p=probs[0])
    dsoftmax = softmax_grad(probs)[action, :]
    dlog = dsoftmax / probs[0, action]
    grad = state.T.dot(dlog[None, :])
    return action, grad
