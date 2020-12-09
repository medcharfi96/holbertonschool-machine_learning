#!/usr/bin/env python3
""" matrix """


def matrix_transpose(matrix):
    """description of function"""
    nw_mat = []
    for col in range(len(matrix[0])):
        mat = []
        for j in range(len(matrix)):
            mat.append(matrix[j][col])
        nw_mat.append(mat)
    return nw_mat
