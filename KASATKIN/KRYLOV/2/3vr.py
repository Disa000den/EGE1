from itertools import *


def f(x, y, z, w):
    return (not(x <= y)) or ((not w) <= (not z)) or w


for x1, x2, x3, x4, x5, x6 in product([0, 1], repeat=6):
    t = (
        (x1, x2, 1, x3, 0),
        (1, 1, x4, x5, 0),
        (x6, 1, 1, 0, 0)
    )
    if len(t) == len(set(t)):
        for p in permutations('xyzw', 4):
            if all(f(**dict(zip(p, line))) == line[-1] for line in t):
                print(*p)