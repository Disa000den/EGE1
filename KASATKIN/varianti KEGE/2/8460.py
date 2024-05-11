from itertools import *


def f(x, y, w, z):
    return ((x == z) or (not(x == w))) and ((y <= x) or (not z))


for x1, x2, x3, x4, x5, x6, x7, x8, x9 in product([0, 1], repeat=9):
    t = (
        (1, x1, 1, 1, 0),
        (x2, 1, x3, 1, 0),
        (x4, 1, 1, 1, 0),
        (1, x5, 1, x6, 0),
        (x7, 1, x8, x9, 0)
    )
    if len(t) == len(set(t)):
        for p in permutations('xyzw', 4):
            if all(f(**dict(zip(p, line))) == line[-1] for line in t):
                print(*p)