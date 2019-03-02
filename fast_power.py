# code: utf-8
import time


def naive_power(base, power, model):
    return base ** power % model


def fast_power(base, power, model):
    res = 1
    power_bin = bin(power)[2:]
    for p in power_bin:
        res = res ** 2 % model
        if p == '1':
            res = res * base % model
    return res


base = 3
power = 3875633
model = 123456787
t = time.time()
r1 = fast_power(base, power, model)
print('elapsed:', time.time()-t)

t = time.time()
r2 = naive_power(base, power, model)
print('elapsed:', time.time()-t)

print(r1, r2)
r1 == r2
