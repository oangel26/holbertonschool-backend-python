#!/usr/bin/env python3
"""
Tasks
"""


import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    The code is nearly identical to wait_n except task_wait_random is
    being called
    """
    lista = []

    for i in range(n):
        x = await task_wait_random(max_delay)

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
    n = 5
    max_delay = 6
    print(asyncio.run(task_wait_n(n, max_delay)))
    
