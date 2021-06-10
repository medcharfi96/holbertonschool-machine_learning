#!/usr/bin/env python3
""" task 10 """
import sklearn.cluster


def kmeans(X, k):
    """
    perform k -mean
    :param X:
    :param k:
    :return:
    """

    k_model = sklearn.cluster.KMeans(n_clusters=k).fit(X)
    clss = k_model.labels_
    C = k_model.cluster_centers_

    return C, clss
