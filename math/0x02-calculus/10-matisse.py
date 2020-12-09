#!/usr/bin/env python3
"""
des
"""


def poly_derivative(poly):
    """description"""
    liste = []
    if len(poly) == 0:
        return None
    elif len(poly) == 1:
        return liste.append(0)
    else:
        for i in range(1, len(poly)):
            if i == 1 and poly[i] != 0:
                liste.append(poly[i])
            elif i != 1 and poly[i] == 0:
                liste.append(0)
            else:
                liste.append(poly[i] * i)
        return liste
