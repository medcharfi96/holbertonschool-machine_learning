#!/usr/bin/env python3
""" concatination de matrice"""


def add_matrices2D(mat1, mat2):
    """description de function """
    if len(mat1) != len(mat2):
        return None
    else:
        new_mat = []
        for i in range(0, len(mat1)):
            if len(mat1[i]) != len((mat2[i])):
                return None
            else:
                row = []
                for j in range(0, len(mat2[i])):
                    row.append(mat1[i][j] + mat2[i][j])
                new_mat.append(row)
    return new_mat
