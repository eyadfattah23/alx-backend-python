#!/usr/bin/env python3
'''Define a type-annotated function sum_mixed_list
which takes a list input_list of floats/ints
as argument returns their sum as a float.'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns the sum of a list as a float .

    Args:
        mxd_lst (list of floats and ints): the number to change.

    Returns:
        float: sum of the list as a float.


    """
    return sum(mxd_lst)
