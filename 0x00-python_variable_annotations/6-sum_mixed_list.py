#!/usr/bin/env python3
"""takes a list of both integers and floats and returns a float."""
from typing import List, Union
import typing


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return sum of array list elements."""

    summation = 0.0
    for i in range(len(mxd_lst)):
        summation += mxd_lst[i]
    return summation
