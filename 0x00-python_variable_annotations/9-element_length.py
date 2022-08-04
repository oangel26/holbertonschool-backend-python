#!/usr/bin/env python3
"""
Let's duck type an iterable object
"""


from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    duck type iterable object
    """
    return [(i, len(i)) for i in lst]


if __name__ == "__main__":
    print(element_length.__annotations__)
