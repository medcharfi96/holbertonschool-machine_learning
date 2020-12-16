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
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            elif type(data) is not list:
                raise TypeError("data must be a list")
            dt = 0
            self.mean = float(sum(data)/len(data))
            for i in data:
                dt += pow((i - self.mean), 2)
            self.stddev = ((dt/(len(data)))**(0.5))
