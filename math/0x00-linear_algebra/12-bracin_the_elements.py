#!/usr/bin/env python3
""" fnt  """


def np_elementwise(mat1, mat2):
    """ description """
    add = mat1.__add__(mat2)
    dub = mat1.__sub__(mat2)
    prd = mat1.__mul__(mat2)
    div = mat1 / mat2
    return(add, dub, prd, div)
