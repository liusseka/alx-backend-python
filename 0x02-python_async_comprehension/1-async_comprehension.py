#!/usr/bin/env python
'''
Task 2
'''
from importlib import import_module as using

async_generator = using('0-async_generator').async_generator


async def async_comprehension():
    """Collect 10 random numbers using
    async comprehensions over async_generator."""
    return [i async for i in async_generator()]
