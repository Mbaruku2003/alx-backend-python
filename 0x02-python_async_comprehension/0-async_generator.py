#!/usr/bin/env python3
"""A coroutine that takes no arguenments."""
import random
from typing import AsyncGenerator
import asyncio


async def async_generator() -> AsyncGenerator[float, None]:
    """loops ten times waiting 1 second each to give a random float."""

    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
