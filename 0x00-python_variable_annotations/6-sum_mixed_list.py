#!/usr/bin/env python3
"""takes a list of both integers and floats and returns a float."""
import typing
from typing import List, Any


def sum_mixed_list(mxd_lst: List[Any]) -> float:
    """Return sum of array list elements."""

    summation = 0.0
    for i in range(len(mxd_lst)):
        summation += mxd_lst[i]
    return summation
