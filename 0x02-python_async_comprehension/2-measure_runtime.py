#!/usr/bin/env python3
'''
Define a coroutine function called async_comprehension
     collect 10 randoms using an async comprehensing over async_generator
     then return the 10 random numbers.
'''
import asyncio
import random
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Coroutine that runs async_comprehension 4 times using asyncio.gather
            (in parallel)

    Returns:
        float: the total runtime.
    """

    start = time.time()

    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())

    return time.time() - start
