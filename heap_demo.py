# code: utf-8

import numpy as np


class Heap:
    def __init__(self):
        self.nums = []

    def len(self):
        return len(self.nums)

    def add(self, x):
        self.nums.append(x)

    def print_as_graph(self):
        print(self.len())
        print(self.nums)

        def pnt(x, n, end=''):
            sx = str(x)
            left = int((n - len(sx)) / 2)
            right = n - left - len(sx)
            print('.'*left + sx + '.'*right, end=end)

        line = 0
        tmp = self.len()
        while tmp > 0:
            tmp -= 2 ** line
            line += 1
        line -= 1
        total = 2 ** line * 6

        nums = self.nums.copy()
        nums.reverse()
        for ln in range(line+1):
            for _ in range(2 ** ln):
                if nums == []:
                    break
                pnt(nums.pop(), total)
            print('')
            total >>= 1


heap = Heap()
any(heap.add(np.random.randint(1000)) for _ in range(30))
heap.print_as_graph()
