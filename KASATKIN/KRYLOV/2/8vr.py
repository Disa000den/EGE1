from itertools import *


def f(x,y,z,w):
    return (not(w <= (not(x <= y)))) and ((not x) <= ((not y) == z))


for x1, x2, x3, x4, x5 in product([0, 1], repeat=5):
    t = (
        (x1, 1, 1, 1, 0),
        (x2, x3, 0, 0, 1),
        (0, x4, x5, 0, 1)
    )
    if len(t) == len(set(t)):
        for p in permutations('xyzw', 4):
            if all(f(**dict(zip(p, line))) == line[-1] for line in t):
                print(*p)