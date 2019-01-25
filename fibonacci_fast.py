# code: utf-8

import numpy as np
import time


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)


def fib_1(n):
    s = [0, 1]
    for _ in range(n-1):
        s.append(sum(s))
        s.pop(0)
    return s[-1]


def fib_9(n):
    m = np.asmatrix([[1, 1], [1, 0]], dtype=np.ndarray)
    m = np.matrix([[1, 1], [1, 0]], dtype=np.ndarray)
    return (m ** n)[0, 1]


v = 20
print(fib(v))
print(fib_1(v))
print(fib_9(v))

v = 20000

t = time.time()
f1 = fib_1(v)
t1 = time.time()-t

t = time.time()
f2 = fib_9(v)
t2 = time.time()-t

print(f1, '\n', f2)
print(t1, t2)
