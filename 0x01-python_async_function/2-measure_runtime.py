#!/usr/bin/env python3
"""
Measure the runtime
"""


import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Create a measure_time function with integers n and max_delay as arguments
    that measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n. Your function should return a float.
    """
    s = time.perf_counter()
    x = asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - s
    return total_time / n


if __name__ == "__main__":
    n = 5
    max_delay = 9

    print(measure_time(n, max_delay))
