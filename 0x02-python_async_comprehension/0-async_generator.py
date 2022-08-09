#!/usr/bin/env python3
"""
Async Generator
"""

import asyncio
import random


async def async_generator():
    for i in range(10):
        await asyncio.sleep(1)
        x = random.uniform(0, 10)
        yield x


if __name__ == "__main__":
    async def print_yielded_values():
        result = []
        async for i in async_generator():
            result.append(i)
        print(result)

    asyncio.run(print_yielded_values())
