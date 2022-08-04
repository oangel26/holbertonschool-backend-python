#!/usr/bin/env python3
"""
Basic annnotations
"""


def floor(n: float) -> int:
    """
    type-annotated function floor which takes a float n as argument and
    returns the floor of the float.
    """
    return int(n)


if __name__ == "__main__":
    import math

    floor = __import__('2-floor').floor

    ans = floor(3.14)

    print(ans == math.floor(3.14))
    print(floor.__annotations__)
    print("floor(3.14) returns {}, which is a {}".format(ans, type(ans)))
