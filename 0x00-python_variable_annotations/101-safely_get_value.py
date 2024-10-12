#!/usr/bin/env python3
"""Given the parameters and the return values,
add type annotations to the function

Hint: look into TypeVar
"""
from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[T, None]:
    """implementation  of dict.get(key) method.

    Args:
        dct (Mapping[Any, T]): _description_
        key (Any): _description_
        default (Union[T, None], optional): _description_. Defaults to None.

    Returns:
        Union[T, None]: _description_
    """
    if key in dct:
        return dct[key]
    else:
        return default
