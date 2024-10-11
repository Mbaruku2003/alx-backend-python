#!/usr/bin/env python3
"""Takes a string and int or float as arg and returns tuple."""
import typing
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """the second elemnt is  a square of the int or float."""

    return (k, float(v**2))
