#!/usr/bin/env python3
"""Takes an integer and returns asyncio.Task."""
import typing
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Takesi an integer and returns a asyncio task."""

    return asyncio.create_task(wait_random(max_delay))
