#!/usr/bin/env python3
'''
Define a coroutine function called async_comprehension
     collect 10 randoms using an async comprehensing over async_generator
     then return the 10 random numbers.
'''
import asyncio
from typing import List
import random
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """get 10 random numbers using an async comprehensing over async_generator

    Returns:
        List[float]: list of 10 random numbers using async_generator
    """
    return [i async for i in async_generator()]
