from itertools import *


def f(x, y, z, w):
    return (x and (not y)) or (x == z) or (not w)


for x1, x2, x3, x4 in product([0, 1], repeat=4):
    t = (
        (0, 1, 1, 0, 0),
        (0, x1, x2, x3, 0),
        (x4, 1, 0, 1, 0)
    )
    if len(t) == len(set(t)):
        for p in permutations('xyzw', 4):
            if all(f(**dict(zip(p, line))) == line[-1] for line in t):
                print(*p)
