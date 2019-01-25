# code: utf-8

import time


class integer_parser:
    def __init__(self, num=13):
        self.num = num
        print('Init interger parser, num as %d' % num)

    def auto_complete(func):
        def _ac(self, num=None):
            if num is None:
                return func(self, self.num)
            return func(self, num)
        return _ac

    def legal_check(func):
        def _lc(self, num):
            try:
                assert(num > 0)
                assert(num % 1 == 0)
            except AssertionError:
                print('Illegal input num as %d.' % num)
                return
            return func(self, num)
        return _lc

    def timing(func):
        def _tm(self, num):
            t = time.time()
            f = func(self, num)
            print('%f secones, elapsed.' % (time.time()-t))
            return f
        return _tm

    @auto_complete
    @legal_check
    @timing
    def is_prime(self, num=None):
        assert(self.is_legal(num))
        return not(any(
            num % e == 0 for e in range(1, num)))

    @auto_complete
    @legal_check
    @timing
    def get_primes_below(self, num=None):
        primes = [1]
        nonprimes = set()
        for c in range(2, num):
            if c in nonprimes:
                continue
            primes.append(c)
            for j in range(2, n):
                if j * c >= n:
                    break
                nonprimes.add(j*c)
        return primes

    @auto_complete
    @legal_check
    @timing
    def get_phi(self, num=None):
        ps = self.get_primes_below(num)
        ps.pop(0)
        phi = num
        while ps:
            p = ps.pop()
            if num % p == 0:
                phi *= (1-1/p)
        return phi


def new_session(n=60):
    print('-' * n)


ip = integer_parser()

new_session()
n = 490000
print(ip.get_phi(n))

new_session()
large_n = 10000
for j in [1, 10, 100]:
    ip.get_primes_below(large_n * j)
