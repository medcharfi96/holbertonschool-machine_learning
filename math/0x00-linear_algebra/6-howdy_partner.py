#!/usr/bin/env python3
""" ajout de tableau"""


def cat_arrays(arr1, arr2):
    """description de function"""
    new_list = []
    for i in range(len(arr1)):
        new_list.append(arr1[i])
    for i in range(len(arr2)):
        new_list.append(arr2[i])
    return new_list
