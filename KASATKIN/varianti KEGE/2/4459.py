from itertools import *


def f(x, y, z, w):
    return ((not x) <= y) and ((not y) == z) and w


for x1, x2, x3, x4, x5, x6, x7, x8 in product([0, 1], repeat=8):
    t = (
        (0, x1, 0, x2, 1),
        (0, x3, x4, x5, 1),
        (x6, 0, x7, x8, 1)
    )
    if len(t) == len(set(t)):
        for p in permutations('xyzw', 4):
            if all(f(**dict(zip(p, line))) == line[-1] for line in t):
                print(*p)