#!/usr/bin/env python3
"""
 More involved type annotations
"""


from typing import Mapping, Any, Union, TypeVar, NewType


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None]) -> Union[Any, T]:
    """
    More involved type annotations
    """
    if key in dct:
        return dct[key]
    else:
        return default


if __name__ == "__main__":
    annotations = safely_get_value.__annotations__

    print("Here's what the mappings should look like")
    for k, v in annotations.items():
        print( ("{}: {}".format(k, v)))
