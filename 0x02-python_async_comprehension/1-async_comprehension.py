#!/usr/bin/env python3
"""Collects 10 random numbers using async comprehension"""
from typing import List
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """collects 10 random numbersusing async comprehensing."""

    result = [x async for x in async_generator()]
    return result
