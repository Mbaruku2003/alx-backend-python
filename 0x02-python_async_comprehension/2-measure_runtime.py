#!/usr/bin/env python3
"""executes async comp 4 times in parallel using asyncio.gather."""
import asyncio
import time
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    starttime = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    total_time = time.perf_counter() - starttime
    return total_time
