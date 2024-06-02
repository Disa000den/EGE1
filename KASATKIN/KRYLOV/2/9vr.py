from itertools import *


def f(x, y, z, w):
    return (not((x <= y) <= w)) and z


for x1, x2, x3, x4, x5, x6, x7 in product([0, 1], repeat=7):
    t = (
        (0, 0, x1, x2, 1),
        (x3, 1, 0, x4, 1),
        (x5, x6, 1, x7, 1)
    )
    if len(t) == len(set(t)):
        for p in permutations('xyzw', 4):
            if all(f(**dict(zip(p, line))) == line[-1] for line in t):
                print(*p)