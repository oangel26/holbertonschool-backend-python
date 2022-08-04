#!/usr/bin/env python3
"""
Complex types - functions
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Type-annotated function make_multiplier that takes a float multiplier
    as argument and returns a function that multiplies a float by multiplier.
    """
    def func(x: float) -> float:
        """
        function that multiplies a float by multiplier
        """
        return x * multiplier

    return func


if __name__ == "__main__":
    print(make_multiplier.__annotations__)
    fun = make_multiplier(2.22)
    print("{}".format(fun(2.22)))
