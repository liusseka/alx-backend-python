#!/usr/bin/env python3
'''
Task 1
'''
import asyncio
import random


async def async_generator():
    """A coroutine that yields a random
    number between 0 and 10 every second."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
