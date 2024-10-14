#!/usr/bin/env python3
"""measures the total edecution time returning a float."""
from typing import List
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """returns total_time / n  as a float."""

    # start the timer
    start_time = time.time()
    # run the wait_n coroutine
    asyncio.run(wait_n(n, max_delay))
    # stop the coroutine
    total_time = time.time() - start_time
    return total_time / n
