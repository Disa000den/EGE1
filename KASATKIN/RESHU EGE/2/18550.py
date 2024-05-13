from itertools import *


def f(x, y, z, w):
    return ((y <= z) or ((not x) and w)) == (w == z)


for x1, x2, x3 in product([0, 1], repeat=3):
    t = (
        (x1, 1, 0, 0, 1),
        (0, 0, 0, 1, 1),
        (0, 1, x2, x3, 1)
    )
    if len(t) == len(set(t)):
        for p in permutations('xyzw', 4):
            if all(f(**dict(zip(p, line))) == line[-1] for line in t):
                print(*p)
