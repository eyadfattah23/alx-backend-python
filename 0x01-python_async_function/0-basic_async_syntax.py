#!/usr/bin/env python3
"""
an asynchronous coroutine
takes in an integer argument (max_delay, with a default = 10) wait_random
waits for a random delay between 0 and max_delay seconds
and eventually returns it.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """waits for a random delay between 0 and max_delay

    Args:
        max_delay (int, optional). Defaults to 10.

    Returns:
        float: time waited for a random delay between 0 and max_delay
    """

    time: float = random.uniform(0, max_delay)
    await asyncio.sleep(time)

    return time
