#!/usr/bin/env python3
"""annotate the function found in readme"""
from typing import Any, Union, Sequence, NoReturn
# The types of the elements of the input are not know


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """returns the first element of the list.

    Args:
        lst (Sequence[Any])

    Returns:
        Union[Any, None]: specify the returned type to be anything
    """
    if lst:
        return lst[0]
    else:
        return None
