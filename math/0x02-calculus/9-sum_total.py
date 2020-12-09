#!/usr/bin/env python3
"""
des
"""


def summation_i_squared(n):
    """dees"""

    x = 0
    if not(isinstance(n, int) or isinstance(n, float)) or n == 0:
        return None
    elif n == 1:
        return 1
    elif n > 1:
        x = pow(n, 2) + summation_i_squared(n-1)
    return(int(x))
