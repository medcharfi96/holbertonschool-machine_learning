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
        if type(data) is not list:
            raise TypeError("data must be a list")
        elif lambtha < 0:
            raise ValueError("lambtha must be a positive value")
        else:
            self.lambtha = float(lambtha)
        if len(data) < 2:
            raise ValueError("data must contain multiple values")
        else:
            self.lambtha = float(sum(data) / len(data))
