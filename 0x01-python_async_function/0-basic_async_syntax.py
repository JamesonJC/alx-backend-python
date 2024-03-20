#!/usr/bin/env python3

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronously waits for a random delay between 0 and max_delay."""
    '''random_number = random.uniform(0, max_delay)
    await asyncio.sleep(random_number)
    return random_number'''

    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time

