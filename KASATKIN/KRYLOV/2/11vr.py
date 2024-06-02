from itertools import *


def f(x, y, z, w):
    return ((x <= y) <= z) or (w <= (y and z))


for x1, x2, x3, x4, x5, x6, x7 in product([0, 1], repeat=7):
    t = (
        (0, x1, x2, 0, 0),
        (1, 0, x3, x4, 0),
        (x5, 1, x6, x7, 0)
    )
    if len(t) == len(set(t)):
        for p in permutations('xyzw'):
            if all(f(**dict(zip(p, line))) == line[-1] for line in t):
                print(*p)