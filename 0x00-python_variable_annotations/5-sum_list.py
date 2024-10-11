#!/usr/bin/env python3
"""Takes a list of floats as arguenment returning their sum as floast."""
import typing
from typing import List


def sum_list(input_list: List[float]) -> float:
    summation = 0.0
    for i in range (len(input_list)):
        summation += input_list[i]
    return summation
