#!/usr/bin/env python3
"""
Let's execute multiple coroutines at the same time with async
"""


import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Async routine called wait_n that takes in 2 int arguments (in this order):
    n and max_delay. You will spawn wait_random n times with the specified
    max_delay.

    wait_n should return the list of all the delays (float values). The list
    of the delays should be in ascending order without using sort() because of
    concurrency.
    """
    lista = []

    for i in range(n):
        x = await wait_random(max_delay)
        
        if (len(lista) == 0):
            lista.append(x)
        elif (len(lista) == 1):
            if (x < lista[0]):
                lista.insert(0, x)
            else:
                lista.append(x)
        else:
            for j in range(len(lista) - 1):
                if (x <= lista[0]):
                    lista.insert(0, x)
                    break
                elif (lista[len(lista) - 1] < x):
                    lista.append(x)
                    break
                elif (lista[j] < x < lista[j + 1]):
                    lista.insert(j + 1, x)
                    break

    return lista


if __name__ == "__main__":
    '''
    Test file for printing the correct output of the wait_n coroutine
    '''
    import asyncio

    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
