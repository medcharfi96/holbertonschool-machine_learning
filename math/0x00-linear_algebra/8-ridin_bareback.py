#!/usr/bin/env python3
""" multiplication de 2 matrice """


def mat_mul(mat1, mat2):
    """description de la function"""
    mat3 = []
    if len(mat1[0]) == len(mat2):
        for a in range(0, len(mat1)):
            rw = []
            for b in range(0, len(mat1[0])):
                el = 0
                for c in range(0, len(mat1[0])):
                    el = el + mat1[a][c] * mat2[c][b]
                    rw.append(el)
            mat3.append(rw)
        return mat3
    else:
        return None
