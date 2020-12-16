#!/usr/bin/env python3
"""
second task
"""


class Exponential:
    """
    class description
    """

    e = 2.7182818285

    def __init__(self, data=None, lambtha=1.):
        """
        function description
        :param data: list
        :param lambtha: value
        """
        if data is None:
            if lambtha < 1:
                raise ValueError("lambtha must be a positive value")
            else:
                self.lambtha = float(lambtha)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(len(data) / sum(data))
