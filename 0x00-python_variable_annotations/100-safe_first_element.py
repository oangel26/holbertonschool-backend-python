#!/usr/bin/env python3
"""
 More involved type annotations
"""


from typing import Any, Union, Sequence


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    method which runs a list
    """
    if lst:
        return lst[0]
    else:
        return None


if __name__ == "__main__":
    print(safe_first_element.__annotations__)
