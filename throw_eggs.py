# code: utf-8


import functools
import time


@functools.lru_cache(maxsize=None)
def throw(floors, eggs):
    if eggs == 1:
        return floors
    if floors == 0:
        return 0
    return min(max(throw(x-1, eggs-1), throw(floors-x, eggs))+1 for x in range(1, floors+1))


print(throw(100, 2))
print(throw(100, 10))


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)


@functools.lru_cache(maxsize=None)
def fib_quick(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_quick(n-1) + fib_quick(n-2)


t = time.time()
print(fib_quick(30))
print(time.time()-t)

t = time.time()
print(fib(30))
print(time.time()-t)
