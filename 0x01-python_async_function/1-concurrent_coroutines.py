#!/usr/bin/env python3

"""Execute multiple coroutines concurrently with asyncio"""

import asyncio
from typing import List

# Importing directly from module
#from 0-basic_async_syntax import wait_random
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn 'wait_random' coroutine 'n' times with the specified 'max_delay'
    and return the list of all the delays (float values).
    """
    '''
    # Creating a list of coroutines
    futures = [wait_random(max_delay) for _ in range(n)]
    # Gathering the results of all coroutines
    delays = await asyncio.gather(*futures)
    return delays'''

    wait_times = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
