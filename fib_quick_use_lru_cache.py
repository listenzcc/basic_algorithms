import functools
import time


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
