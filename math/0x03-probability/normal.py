#!/usr/bin/env python3
"""
third task
"""


class Normal:
    """
    class description
    """
    e = 2.7182818285
    pi = 3.1415926536

    def __init__(self, data=None, mean=0., stddev=1.):
        """
        function description l3asba ya wideeed w nik lsbeh
        :param data: list
        :param mean: float
        :param stddev: int
        """
        self.data = data
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            else:
                self.mean = float(mean)
                self.stddev = float(stddev)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            test = 0
            self.mean = float(sum(data)/len(data))
            for i in data:
                test += pow((i - self.mean), 2)
            self.stddev = ((test/(len(data)))**(0.5))

    def z_score(self, x):
        """
        funcd
        """
        return ((x - self.mean)/self.stddev)

    def x_value(self, z):
        """
        function desc
        :param z:
        :return:
        """
        return (self.mean + (z * self.stddev))

    def pdf(self, x):
        """
        function desc
        :param x: int or float
        :return: the pdf result
        """
        return pow(Normal.e, -(pow((x - self.mean), 2) /
                               (2 * (pow(self.stddev, 2)))))/(pow(
                                (2 * Normal.pi), 1 / 2) * self.stddev)
