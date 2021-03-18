#!/usr/bin/env python3
""" task 1 """


def inv(i, row, matrix):
    """
    get the row
    :param i:
    :param row:
    :param matrix:
    """
    sub_m = []
    for r in row:
        aux = []
        for c in range(len(matrix)):
            if c != i:
                aux.append(r[c])
        sub_m.append(aux)
    return sub_m


def determinant(matrix):
    """
    fonction de calcue de determinant
    :param matrix: matrice
    """
    if matrix == [[]]:
        return 1
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a list of lists")
    if len(matrix[0]) != len(matrix):
        raise ValueError("matrix must be a square matrix")
    for i in matrix:
        if type(i) is not list:
            raise TypeError("matrix must be a list of lists")
        elif len(i) != len(matrix):
            raise ValueError("matrix must be a square matrix")
    if len(matrix) == 1:
        return matrix[0][0]

    if len(matrix) == 2:
        a = (matrix[1][1] * matrix[0][0]) - (matrix[1][0] * matrix[0][1])
        return a
    determ = 0
    for i, j in enumerate(matrix[0]):
        row = [rw for rw in matrix[1:]]
        mini_mat = []
        mini_mat = inv(i, row, matrix)

        determ = determ + (j * (-1) ** i * determinant(mini_mat))

    return determ


def new_sub_mtr(c, seb, matrix):
    """

    :param i:
    :param k:
    :param matrix:
    :return:
    """
    mini_mat = []
    for r in range(len(matrix)):
        case = []
        for co in range(len(matrix)):
            if seb != r and c != co:
                case.append(matrix[r][co])
        if len(case) > 0:
            mini_mat.append(case)
    return (mini_mat)


def minor(matrix):
    """

    :param matrix:
    :return:
    """
    if len(matrix) == 1:
        return [[1]]
    if matrix == []:
        raise TypeError("matrix must be a list of lists")
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a list of lists")
    if len(matrix[0]) != len(matrix):
        raise ValueError("matrix must be a non-empty square matrix")
    for i in (matrix):
        if type(i) is not list:
            raise TypeError("matrix must be a list of lists")
        elif len(i) != len(matrix):
            raise ValueError("matrix must be a non-empty square matrix")

    retour = []
    for seb in range(len(matrix)):
        case = []
        for c in range(len(matrix[0])):
            case.append(determinant(new_sub_mtr(c, seb, matrix)))
        retour.append(case)
    return minor
