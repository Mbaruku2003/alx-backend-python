#!/usr/bin/env python3
"""Here we are being tested on the basics of using asyncio."""
import asyncio
import random


async def wait_random(max_delay=10):
    """awaits for a random delay between 0 and max_delay."""

    return random.randint(0, max_delay)
