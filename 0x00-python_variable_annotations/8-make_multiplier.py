#!/usr/bin/env python3
'''Define a type-annotated function make_multiplier
takes a float multiplier as argument
returns a function that multiplies a float by multiplier'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ returns a function that multiplies a float by multiplier

    Args:
        multiplier (float): _description_

    Returns:
        Callable: _description_
    """
    def multiply(multiplier_1: float) -> float:
        return multiplier_1 * multiplier
    return multiply
