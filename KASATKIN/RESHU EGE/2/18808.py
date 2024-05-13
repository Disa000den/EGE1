from itertools import *


def f(x, y, w ,z):
    return (x and (not y)) or (y == z) or w


for x1, x2, x3, x4, x5, x6, x7, x8 in product([0, 1], repeat=8):
    t = (
        (x1, x2, x3, 1, 0),
        (1, x4, x5, x6, 0),
        (1, 1, x7, x8, 0)
    )
    if len(t) == len(set(t)):
        for p in permutations('xywz', 4):
            if all(f(**dict(zip(p, line))) == line[-1] for line in t):
                print(*p)