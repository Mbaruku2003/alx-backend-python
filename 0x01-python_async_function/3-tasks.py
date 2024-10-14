#!/usr/bin/env python3
"""Takes an integer and returns asyncio.Task."""
import typing
wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Takes an integer and returns a asyncio task."""

    return asyncio.Task(wait_random(max_delay))
