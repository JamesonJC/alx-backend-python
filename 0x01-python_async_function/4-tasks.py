#!/usr/bin/env python3
"""Execute multiple coroutines at the same time with async"""

from typing import List
import asyncio

# Importing directly from module
#from 3-tasks import task_wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay
    and returns the list of all the delays (float values).
    """
    '''
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return delays
    '''
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
