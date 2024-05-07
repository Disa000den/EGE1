#((y → x) ≡ (x → w)) ∧ (z ∨ x).
from itertools import *


def f(x, y, w, z):
    return ((y <= x) == (x <= w)) and (z or x)


for x1, x2, x3, x4, x5, x6 in product([0, 1], repeat=6):
    t = (
        (0, x1, x2, 0, 1),
        (0, 0, 0, x3, 1),
        (x4, x5, 0, x6, 1)
    )
    if len(t) == len(set(t)):
        for p in permutations('xywz', 4):
            if all(f(**dict(zip(p, line))) == line[-1] for line in t):
                print(*p)