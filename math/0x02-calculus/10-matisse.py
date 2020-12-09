#!/usr/bin/env python3
"""
des
"""


def poly_derivative(poly):
    """description"""
    liste = []
    liste2 = [0]
    if type(poly) is not list or poly is None:
        return None
    for z in range(len(poly)):
        if poly[z] is not int or poly[z] is not float:
            return None
    if len(poly) == 0:
        return None
    elif len(poly) == 1:
        return liste2
    else:
        for i in range(1, len(poly)):
            if i == 1 and poly[i] != 0:
                liste.append(poly[i])
            elif i != 1 and poly[i] == 0:
                liste.append(0)
            else:
                liste.append(poly[i] * i)
        return liste
