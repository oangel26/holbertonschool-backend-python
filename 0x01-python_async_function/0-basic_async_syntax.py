#!/usr/bin/env python3
"""
The basics of async
"""

import random, asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that takes in an integer argument
    (max_delay, with a default value of 10) named wait_random
    that waits for a random delay between 0 and max_delay
    (included and float value) seconds and eventually returns it.
    """
    return float(random.uniform(0, max_delay))


if __name__ == "__main__":
    import asyncio

    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))
