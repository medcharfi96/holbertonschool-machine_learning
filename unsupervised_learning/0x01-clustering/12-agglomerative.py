#!/usr/bin/env python3
""" task 12 """


import scipy.cluster.hierarchy
import matplotlib.pyplot as plt


def agglomerative(X, dist):
    """
    performe clustring
    :param X:
    :param dist:
    :return:
    """

    linkage = scipy.cluster.hierarchy.linkage
    dendogram = scipy.cluster.hierarchy.dendrogram
    cluster = scipy.cluster.hierarchy.fcluster

    Z = linkage(X, "ward")

    dendogram(Z, color_threshold=dist, no_labels=False, ax=None)
    plt.show()

    clss = cluster(Z, dist, criterion="distance")
    return clss
