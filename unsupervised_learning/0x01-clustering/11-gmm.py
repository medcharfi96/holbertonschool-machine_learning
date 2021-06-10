#!/usr/bin/env python3
"""task 11 """


import sklearn.mixture


def gmm(X, k):
    """
    calcule gmm
    :param X:
    :param k:
    :return:
    """

    mixture = sklearn.mixture.GaussianMixture(n_components=k)
    g = mixture.fit(X)
    m = g.means_
    S = g.covariances_
    pi = g.weights_
    clss = mixture.predict(X)
    bic = mixture.bic(X)

    return pi, m, S, clss, bic
