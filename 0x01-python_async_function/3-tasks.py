#!/usr/bin/env python3
"""
Tasks
"""


import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> None:
    """
    Function task_wait_random that takes an integer max_delay
    and returns a asyncio.Task.
    """
    t = asyncio.create_task(wait_random(max_delay))
    return t


if __name__ == "__main__":
    async def test(max_delay: int) -> float:
        task = task_wait_random(max_delay)
        await task
        print(task.__class__)

    asyncio.run(test(5))
