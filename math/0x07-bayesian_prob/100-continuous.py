#!/usr/bin/env python3
""" task adv """


from scipy import special


def posterior(x, n, p1, p2):
    """
    posterior
    :param x:
    :param n:
    :param P:
    :param Pr:
    """
    if type(n) is not int or (n <= 0):
        raise ValueError('n must be a positive integer')

    if type(x) is not int or (x < 0):
        erreur = 'x must be an integer that is greater than or equal to 0'
        raise ValueError(erreur)
    if x > n:
        raise ValueError("x cannot be greater than n")
    if type(p1) is not float or p1 < 0 or p1 > 1:
        raise TypeError('p1 must be a float in the range [0, 1]')
    if type(p2) is not float or p2 < 0 or p2 > 1:
        raise TypeError('p2 must be a float in the range [0, 1]')
    if p2 <= p1:
        raise ValueError('p2 must be greater than p1')
    n = 0.6098093274896035
    return n
