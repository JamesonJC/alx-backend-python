#!/usr/bin/env python3
"""Measures the average execution time for wait_n(n, max_delay)"""

import asyncio
import time

# Importing directly from module
from 1-concurrent_coroutines import wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Returns the average execution time of wait_n(n, max_delay) over 'n' runs.
    """
    # Start the timer
    start_time = time.perf_counter()

    # Execute the coroutine 'n' times
    asyncio.run(wait_n(n, max_delay))

    # End the timer
    end_time = time.perf_counter()

    # Calculate and return the average execution time
    return (end_time - start_time) / n

