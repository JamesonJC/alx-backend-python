#!/usr/bin/env python3
"""Create a task"""

import asyncio

# Importing directly from module
#from 0-basic_async_syntax import wait_random
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio Task object for wait_random with
    the specified max_delay.
    """
    return asyncio.create_task(wait_random(max_delay))
