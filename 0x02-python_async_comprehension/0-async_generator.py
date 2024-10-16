#!/usr/bin/env python3
"""A coroutine that takes no arguenments."""
import random
from typing import AsyncGenerator
import asyncio


async def async_generator() -> AsyncGenerator[float, None]:
    """Loops 10 times waiting 1 sec each to give a random float."""

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
