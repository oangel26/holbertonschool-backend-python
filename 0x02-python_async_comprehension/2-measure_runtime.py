#!/usr/bin/env python3
"""
 Run time for four parallel comprehensions
"""


import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine which executes async_comprehension four times in parallel
    using asyncio.gather and measure the total runtime and return it.
    """
    s = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    total_time = time.perf_counter() - s

    return total_time


if __name__ == "__main__":
    async def main():
        return await(measure_runtime())

    print(
        asyncio.run(main())
    )
