from math import *
from sys import *
from functools import lru_cache
setrecursionlimit(10000)


@lru_cache(None)
def f(n):
    if n == 0:
        return 0
    if n > 0 and n % 10 == 0:
        return f(n // 10)
    if n > 0 and n % 10 > 0 and floor(log10(n)) % 2 == 0:
        return f(n - 1) - 1
    if n > 0 and n % 10 > 0 and floor(log10(n)) % 2 != 0:
        return f(n - 1) + 1


cnt = 0
for n in range(10 ** 6 + 1):
    if f(n) == 0:
        cnt += 1
print(cnt)