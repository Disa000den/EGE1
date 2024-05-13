from itertools import *


def f(x, y, z, w):
    return (not(y <= x)) or (y == w) or z


for x1, x2, x3, x4, x5, x6 in product([0, 1], repeat=6):
    t = (
        (x1, x2, 1, 1, 0),
        (x3, x4, 1, x5, 0),
        (0, 1, x6, 1, 0)
    )
    if len(t) == len(set(t)):
        for p in permutations('xyzw', 4):
            if all(f(**dict(zip(p, line))) == line[-1] for line in t):
                print(*p)