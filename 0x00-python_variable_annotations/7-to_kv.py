#!/usr/bin/env python3
'''Define a type-annotated function sum_mixed_list
which takes a list input_list of floats/ints
as argument returns their sum as a float.'''
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuple. The first element of the tuple is the string k

    Args:
        k (str): tuple(0)
        v (Union[int, float]): root(tuple(1))

    Returns:
        tuple: _description_
    """
    return (k, float(v**2))
