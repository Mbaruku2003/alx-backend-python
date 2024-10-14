#!/usr/bin/env python3
"""an async routine tht tkes in two arguenments n & max_delay."""
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax.py').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """spawn wait_random n times the specified max_delay."""

    #create a list of tasks to be run concurently
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    #initialise an empty list to store the delays
    delays = []
    #loop throught the result as they complete and add their results to e list
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays = .append(delay)

    return delays
