# code: utf-8

import math
import random
import time


def fast_power(base, power, model):
    res = 1
    power_bin = bin(power)[2:]
    for p in power_bin:
        res = res ** 2 % model
        if p == '1':
            res = res * base % model
    return res


def miller_rabin_test(p, a):
    # protect code
    assert(p % 1 == 0)
    assert(p > 0)
    # naive assuming
    print('-' * 60)
    print('testing:', p)
    if p == 1:
        return True
    if p == 2:
        return True
    if p % 2 == 0:
        return False

    # now we begin
    u = p-1
    t = 0
    while u % 2 == 0:
        u //= 2
        t += 1
    assert(u * 2 ** t == p-1)
    print('\t%d = %d x 2^%d' % (p-1, u, t))

    for k in range(t+1):
        print('\t(%d/%d):' % (k+1, t+1), end=' ')
        if k == 0:
            r = fast_power(a, u, p)
            print('(%d^%d)(mod %d) = %d (mod %d)' % (a, u, p, r, p))
            continue
        else:
            r0 = r
            r1 = fast_power(r, 2, p)
            print('(%d^2)(mod %d) = %d (mod %d)' % (r, p, r1, p), end=' ')
            r = r1
        if r == 1 and (r0 not in [1, p-1]):
            print('fail.')
            return False
        print('pass.')

    # now, r = a^(p-1) % p, here we end
    if r == 1:
        return True
    else:
        return False


def is_prime(p):
    a_list = [random.randint(2, p-1) for _ in range(5)]
    return all(miller_rabin_test(p, a) for a in a_list)


def compute_power(a, p, m):
    result = 1
    p_bin = bin(p)[2:]
    length = len(p_bin)
    for i in range(0, length):
        result = result**2 % m
        if p_bin[i] == '1':
            result = result * a % m
    return result


def miller_rabin_witness(a, p):
    if p == 1:
        return False
    if p == 2:
        return True

    n = p - 1
    t = int(math.floor(math.log(n, 2)))
    u = 1
    while t > 0:
        u = n // 2**t
        if n % 2**t == 0 and u % 2 == 1:
            break
        t = t - 1
    print(a, n, u, t)

    b1 = b2 = compute_power(a, u, p)
    for i in range(1, t + 1):
        b2 = b1**2 % p
        print(b1, b2)
        if b2 == 1 and b1 != 1 and b1 != (p - 1):
            print('x:', b1, b2)
            return False
        b1 = b2
    if b1 != 1:
        return False

    return True


def prime_test_miller_rabin(p, k):
    while k > 0:
        a = random.randint(2, p - 1)
        print(a)
        if not miller_rabin_witness(a, p):
            return False
        k = k - 1
    return True


test = [random.randint(5, 100) for _ in range(10)]
r1 = [prime_test_miller_rabin(t, 5) for t in test]
r2 = [is_prime(t) for t in test]
print(test)
print(r1)
print(r2)
