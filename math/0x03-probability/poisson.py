#!/usr/bin/env python3
"""
first task
"""


class Poisson:
    """
    class description
    """

    e = 2.7182818285

    def __init__(self, data=None, lambtha=1.):
        """
        function description
        :param data: list
        :param lambtha: number
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            else:
                self.lambtha = float(lambtha)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """
        fuction description
        :param k: int
        """
        e = 2.7182818285
        if int(k) > 0:
            k = int(k)
        else:
            return(0)
        nb = 1
        for i in range(1, k + 1):
            nb = nb * i
        return(((pow(e, -self.lambtha)) * (pow(self.lambtha, k))) / nb)
