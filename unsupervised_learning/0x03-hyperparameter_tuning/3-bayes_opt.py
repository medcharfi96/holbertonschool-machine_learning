#!/usr/bin/env python3
""" task 4 """


import numpy as np
GP = __import__('2-gp').GaussianProcess


class BayesianOptimization():
    """ classe de performance de bayesian  """

    def __init__(self, f, X_init, Y_init, bounds,
                 ac_samples, l=1, sigma_f=1, xsi=0.01, minimize=True):
        """
        constructeur parametré
        :param f:
        :param X_init:
        :param Y_init:
        :param bounds:
        :param ac_samples:
        :param l:
        :param sigma_f:
        :param xsi:
        :param minimize:
        """

        self.f = f
        self.gp = GP(X_init, Y_init, l, sigma_f)
        X_s = np.linspace(bounds[0], bounds[1], num=ac_samples, retstep=False)
        self.X_s = X_s.reshape(-1, 1)
        self.xsi = xsi
        self.minimize = minimize
