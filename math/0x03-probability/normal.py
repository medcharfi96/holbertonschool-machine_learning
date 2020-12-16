#!/usr/bin/env python3
"""
third task
"""


class Normal:
    """
    class description
    """
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
        fuction desc
        :param x: int
        """
        return (x - self.mean) / self.stddev
