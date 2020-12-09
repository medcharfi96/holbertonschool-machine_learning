#!/usr/bin/env python3
"""concatination de tableau"""


def add_arrays(arr1, arr2):
    """ descriptionde function"""
    if len(arr1) != len(arr2):
        return None
    else:
        new_list = []
        for i in range(len(arr1)):
            new_list.append(arr1[i] + arr2[i])
    return new_list
