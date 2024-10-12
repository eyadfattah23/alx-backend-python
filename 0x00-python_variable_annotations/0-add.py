#!/usr/bin/env python3
'''Define a type-annotated function add:
takes a float a and a float b as arguments and returns their sum as a float'''


def add(a: float, b: float) -> float:
    """sum of a + b in float. 

    Args:
        a (float)
        b (float)

    Returns:
        float: result of a+b
    """
    return a + b
