#!/usr/bin/env python3
'''
Define a coroutine function called async_generator
    loop 10 times, each time asynchronously wait 1 second,
        then yield a random number between 0 and 10.
'''
import asyncio
from typing import AsyncGenerator
import random


async def async_generator() -> AsyncGenerator[float, None]:
    """loop 10 times, each time asynchronously wait 1 second,
        then yield a random number

    Yields:
        Generator[float, None]: _description_
    """

    for i in range(10):
        await asyncio.sleep(1)  # Simulate a delay
        yield random.uniform(0, 10)
