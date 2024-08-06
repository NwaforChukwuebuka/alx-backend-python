#!/usr/bin/env python3
'''Task 1. Let's execute multiple coroutines at the same time with async
'''
import asyncio
import random
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    '''Spawn wait_random() n times
    '''
    count = 0
    delay_list = []
    while (count < n):
        float_delay = await task_wait_random(max_delay)
        delay_list.append(float_delay)
        count += 1

    return sorted(delay_list)
