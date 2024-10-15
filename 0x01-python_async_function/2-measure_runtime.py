#!/usr/bin/env python3
'''Define a measure_time function with integers n and max_delay
measures the total execution time for wait_n(n, max_delay),
and returns total_time / n. function should return a float.

'''
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measures the total execution time for wait_n(n, max_delay)

    Args:
        n (int): _description_
        max_delay (int): _description_

    Returns:
        float: total_time / n
    """

    start = time.time()

    asyncio.run(wait_n(n, max_delay))

    end = time.time()

    elapsed = end - start

    return elapsed/n
