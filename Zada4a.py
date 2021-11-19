#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit
from functools import lru_cache


@lru_cache
def factorial(number=1):
    for i in range(1, number+1):
        number += i


@lru_cache
def fib(number=1):
    if number == 1:
        return 1
    return number + fib(number - 1)


print(timeit.timeit(stmt=factorial, number=999999))
print(timeit.timeit(stmt=fib, number=999999))
