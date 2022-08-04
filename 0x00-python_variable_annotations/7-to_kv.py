#!/usr/bin/env python3
"""
Complex types - string and int/float to tuple
"""


from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple:
    """
    Type-annotated function to_kv that takes a string k and an int OR float v
    as arguments and returns a tuple.
    """
    return (k, v ** 2)


if __name__ == "__main__":
    print(to_kv.__annotations__)
    print(to_kv("eggs", 3))
    print(to_kv("school", 0.02))
