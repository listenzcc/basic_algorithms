# code: utf-8

import numpy as np


class Heap:
    def __init__(self):
        self.nums = []

    def len(self):
        return len(self.nums)

    def append(self, x):
        self.nums.append(x)

    def legal_j(self, j):
        if j < 0:
            return False
        if j >= self.len():
            return False
        return True

    def print_node(self, j):
        assert(self.legal_j(j))
        print(','.join(str(self.nums[x])
                       for x in [j, j*2+1, j*2+2] if self.legal_j(x)))

    def print_heap(self):
        print('-' * 60)
        print(self.len())
        print(self.nums)
        for j in range(self.len()):
            self.print_node(j)

    def print_as_graph(self):
        print('-' * 60)
        print(self.len())
        print(self.nums)

        def pnt(x, n, end=''):
            sx = str(x)
            left = int((n - len(sx)) / 2)
            left_1 = int(left/2)
            left_2 = left - left_1
            right = n - left - len(sx)
            right_1 = int(right/2)
            right_2 = right - right_1
            print(' '*left_1 + '_'*left_2 + sx +
                  '_'*right_1 + ' '*right_2, end=end)

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
any(heap.append(np.random.randint(1000)) for _ in range(20))
heap.print_as_graph()
heap.print_heap()
