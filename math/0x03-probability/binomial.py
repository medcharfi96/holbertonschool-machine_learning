#!/usr/bin/env python3
"""
final task
"""


class Binomial:
    """
    class description
    """
    e = 2.7182818285
    pi = 3.1415926536

    def __init__(self, data=None, n=1, p=0.5):
        """
        init function
        :param data: list
        :param n: int
        :param p: float
        """
        self.data = data
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            elif p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
            else:
                self.n = int(n)
                self.p = float(p)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            test = 0
            moy = float(sum(data)/len(data))
            for i in data:
                test += pow((i - moy), 2)
                self.n = int(round(moy / (1 - ((test / len(data)) / moy))))
                self.p = float(moy / self.n)

    def fac(nika):
        """
        fact
        """
        res = 1
        for x in range(1, nika + 1):
            res = x * res
        return(res)

    def pmf(self, k):
        """
        description f jbal
        :param k: int
        """
        if int(k) > 0:
            k = int(k)
        else:
            return(0)
        fok = (Binomial.fac(self.n)) /\
              ((Binomial.fac(k)) * (Binomial.fac(self.n - k)))
        return fok * (self.p ** k) * ((1 - self.p) ** (self.n - k))
