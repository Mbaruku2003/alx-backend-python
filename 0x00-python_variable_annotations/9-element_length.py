#!/usr/bin/env python3
"""annotate prameters and return values with appropriate types."""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Element length findsthe length of a list."""
    return [(i, len(i)) for i in lst]
