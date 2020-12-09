#!/usr/bin/env python3
""" addition de 2 matrice """


def cat_matrices2D(mat1, mat2, axis=0):
    """description de function"""
    new_mat = []
    if (axis == 0):
        if (len(mat1[0]) != len(mat2[0])):
            return None
        else:
            new_mat = [[ii for ii in col] for col in mat1] +\
                      [[jj for jj in col1] for col1 in mat2]
    else:
        if len(mat1) != len(mat2):
            return None
        else:
            for i in range(len(mat1)):
                s = mat1[i] + mat2[i]
                new_mat.append(s)
    return new_mat
