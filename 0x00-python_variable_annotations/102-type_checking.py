#!/usr/bin/env python3
"""code to be checked using mypy"""

from typing import Tuple, List, Any


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """returns a deatailed version of the list given"""
    zoomed_in: List = [
        (item for item in lst
         for i in range(int(factor)))
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, int(3.0))
