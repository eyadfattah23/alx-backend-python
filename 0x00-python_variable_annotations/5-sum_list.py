#!/usr/bin/env python3
'''Define a type-annotated function sum_list
which takes a list input_list of floats
as argument returns their sum as a float.'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    """returns the sum of a list as a float .

    Args:
        input_list (list of floats): the number to change.

    Returns:
        float: sum of the list as a float.


    """
    return sum(input_list)
