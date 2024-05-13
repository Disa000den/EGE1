from itertools import *


def f(x, y, w, z):
    return ((x and y) or (y and z)) == ((x <= w) and (w <= z))


for x1, x2 in product([0, 1], repeat=2):
    t = (
        (0, 1, 1, 1, 1),
        (0, 1, 0, x1, 1),
        (0, 1, 0, x2, 1)
    )
    if len(t) == len(set(t)):
        for p in permutations('xywz', 4):
            if all(f(**dict(zip(p, line))) == line[-1] for line in t):
                print(*p)
