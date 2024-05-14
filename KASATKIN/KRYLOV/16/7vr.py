from math import *
from sys import *


setrecursionlimit(100000)
def f(n):
    if n < 3:
        return 1
    if n > 2 and n % 2 != 0:
        return f(n - 1) + f(n - 2)
    if n > 2 and n % 2 == 0:
        return sum(f(i) for i in range(1, n))


print(f(24))
