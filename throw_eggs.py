# code: utf-8

import functools
import time
import sys

sys.setrecursionlimit(1500)


@functools.lru_cache(maxsize=None)
def throw(floors, eggs):
    # calculate minimal times of trying
    # without lru_cache, this will be very slow
    if eggs == 1:
        return floors
    if floors == 0:
        return 0
    return min(max(throw(x-1, eggs-1), throw(floors-x, eggs))+1 for x in range(1, floors+1))


def mk_table(floors, eggs):
    table = list(list(0 for _ in range(eggs+1)) for __ in range(floors+1))
    for f in range(floors+1):
        table[f][0] = 0
        table[f][1] = f
    for e in range(2, eggs+1):
        for f in range(1, floors+1):
            table[f][e] = 1 + min(max(table[x-1][e-1], table[f-x][e])
                                  for x in range(1, floors+1))
    return table


def max_height(n, m):
    # max height to test with n eggs, m floors
    # n, eggs indifferent
    # m, floors
    h, t = 0, 1
    for i in range(1, n + 1):
        t = t * (m - i + 1) // i
        h += t
    return h


print(max_height(2, 14))

t = time.time()
# print('-' * 60)
# for j, e in enumerate(mk_table(100, 10)):
#    print(j, '\t', e)
table = mk_table(100, 10)
print(table[100][2])
print(table[100][10])
print(time.time() - t)

t = time.time()
print(throw(100, 2))
print(throw(105, 2))
print(throw(100, 10))
print(time.time() - t)
