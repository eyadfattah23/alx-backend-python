#!/usr/bin/env python3
'''Define a type-annotated function concat:
takes a string str1 and a string str2 as arguments
returns a concatenated string'''


def concat(str1: str, str2: str) -> str:
    """concat of str1 + str1 in str.

    Args:
        str1 (str)
        str2 (str)

    Returns:
        str: result of concatenation of str1 and str2
    """
    return str1+str2
