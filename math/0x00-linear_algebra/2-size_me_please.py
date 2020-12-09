#!/usr/bin/env python3
""" matrice taille"""


def matrix_shape(matrix):
    """ description"""
    new = []
    while isinstance(matrix, list):
        new.append(len(matrix))
        matrix = matrix[0]
    return new
