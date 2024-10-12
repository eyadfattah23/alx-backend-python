#!/usr/bin/env python3
"""annotate the function found in readme"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return a list of (value, idx) tuples of all elements in lst

    Args:
        lst (list)

    Returns:
        list of tuples
    """
    return [(i, len(i)) for i in lst]
