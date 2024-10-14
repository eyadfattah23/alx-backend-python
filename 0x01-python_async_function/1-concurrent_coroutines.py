#!/usr/bin/env python3
'''
Define an async routine called wait_n
takes in 2 int arguments (in this order): n and max_delay.
spawn wait_random n times with the specified max_delay.
'''
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """spawn wait_random n times with the specified max_delay

    Args:
        n (int)
        max_delay (int)

    Returns:
        List[float]: the list of all the delays,
                order without using sort() because of concurrency.
    """
    tasks = []
    results = []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    return [await task for task in asyncio.as_completed(tasks)]
