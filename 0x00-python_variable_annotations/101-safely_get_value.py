#!/usr/bin/env python3
"""
 More involved type annotations
"""

from typing import Mapping, Any, Union, TypeVar, NewType


T = TypeVar('T')


NoneType = NewType('NoneType', None)


def safely_get_value(dct: Mapping, key: Any, default: Union[T, NoneType]) -> Union[Any, T]:
    """
    Method that iterates over a dict
    """
    if key in dct:
        return dct[key]
    else:
        return default
