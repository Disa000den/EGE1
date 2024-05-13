from functools import lru_cache
from sys import *
setrecursionlimit(10000)

@lru_cache(None)
def f(n):
    if n == 0:
        return 0
    if n > 0 and n % 2 == 0:
        return f(n // 10) + n % 10
    if n % 2 != 0:
        return f(n // 10)


cnt = 0
for n in range(10 ** 9, 2 * 10 ** 9 + 1):
    if f(n) == 0:
        cnt += 1
print(cnt)
#эта залупа должна обработать 1млрд операций, что пздц долго, так что в жопу